"""
Package Dependency Resolver
============================
Algorithm: Kahn's Topological Sort with alphabetically-sorted selection rounds.

PROBLEM STATEMENT
-----------------
Given a set of packages and their dependencies, determine a valid installation
order such that:
  1. Every package is installed AFTER all of its dependencies.
  2. Within each "round" of installable packages (those whose deps are all met),
     packages are selected in alphabetical order.

This is NOT the same as sorting the final output list alphabetically.
The round-by-round alphabetical constraint affects which packages get resolved
first, which in turn affects which packages become eligible in later rounds.

ALGORITHM OVERVIEW (Kahn's + sorted queue)
-------------------------------------------
1. Build a dependency graph: for each package, track which packages it depends on.
2. Compute "in-degree": the number of unresolved dependencies each package has.
3. Initialize a sorted queue with all packages that have in-degree == 0 (no deps).
4. While the queue is non-empty:
     a. Sort the queue alphabetically (this is the per-round constraint).
     b. Pop the first (alphabetically smallest) package.
     c. Append it to the result.
     d. For each package that depends on this one, decrement its in-degree.
     e. If a package's in-degree reaches 0, add it to the queue.
5. If the result contains all packages, we're done.
   If not, a cycle exists in the dependencies (unsatisfiable).

TIME COMPLEXITY: O(N log N + E), where N = packages, E = dependency edges.
  - The log N factor comes from sorting the queue at each step.

EXAMPLE
-------
Packages and their dependencies:
  flask     -> [werkzeug, jinja2, click]
  werkzeug  -> []
  jinja2    -> [markupsafe]
  click     -> []
  markupsafe-> []
  requests  -> [urllib3, certifi]
  urllib3   -> []
  certifi   -> []

Expected round-by-round resolution:
  Round 1 eligible (in-degree 0): certifi, click, markupsafe, urllib3, werkzeug
    -> sorted: [certifi, click, markupsafe, urllib3, werkzeug]
    -> install certifi  -> urllib3 still has in-degree 1 (certifi was its dep? no)
    -> Actually: certifi, click, markupsafe, urllib3, werkzeug all installed first
  Round 2 eligible: jinja2 (markupsafe done), requests (urllib3+certifi done)
    -> sorted: [jinja2, requests]
    -> install jinja2, requests
  Round 3 eligible: flask (werkzeug, jinja2, click all done)
    -> install flask

Final order: [certifi, click, markupsafe, urllib3, werkzeug, jinja2, requests, flask]
"""


from collections import defaultdict


def resolve_dependencies(packages: dict[str, list[str]]) -> list[str]:
    """
    Resolve package installation order respecting dependencies.
    Within each eligible round, packages are selected alphabetically.

    Args:
        packages: A dict mapping package name -> list of its dependencies.
                  Example: {"flask": ["werkzeug", "jinja2"], "werkzeug": []}

    Returns:
        A list of package names in valid installation order.

    Raises:
        ValueError: If a cyclic dependency is detected (unsatisfiable graph).
        ValueError: If a dependency references an undeclared package.
    """

    # -------------------------------------------------------------------------
    # STEP 0: Validate that all referenced dependencies are declared.
    # This prevents silent failures where a typo in a dep name causes a package
    # to appear to have no blockers, leading to a wrong install order.
    # -------------------------------------------------------------------------
    all_packages = set(packages.keys())
    for pkg, deps in packages.items():
        for dep in deps:
            if dep not in all_packages:
                raise ValueError(
                    f"Package '{pkg}' depends on '{dep}', "
                    f"but '{dep}' is not declared in the package list."
                )

    # -------------------------------------------------------------------------
    # STEP 1: Build a reverse-adjacency list ("dependents" map).
    # For each package P, we want to know: which packages are WAITING on P?
    # When P is installed, we use this to update their in-degrees.
    #
    # Example: if flask depends on werkzeug, then:
    #   dependents["werkzeug"] contains "flask"
    # -------------------------------------------------------------------------
    dependents: dict[str, list[str]] = defaultdict(list)
    # in_degree[pkg] = number of unresolved dependencies pkg still has
    in_degree: dict[str, int] = {pkg: 0 for pkg in packages}

    for pkg, deps in packages.items():
        for dep in deps:
            # dep must be installed before pkg, so pkg is a dependent of dep
            dependents[dep].append(pkg)
            # pkg has one more unresolved dependency
            in_degree[pkg] += 1

    # -------------------------------------------------------------------------
    # STEP 2: Initialize the queue with all packages that have no dependencies.
    # These are immediately installable.
    # We use a plain list and sort it at each step (rather than a heap) because:
    #   - The queue is typically small
    #   - It keeps the "sorted round" semantics explicit and readable
    # -------------------------------------------------------------------------
    # Collect packages with no dependencies (in_degree == 0)
    ready_queue: list[str] = [pkg for pkg, deg in in_degree.items() if deg == 0]

    # -------------------------------------------------------------------------
    # STEP 3: Main Kahn's loop — process the queue until empty.
    # -------------------------------------------------------------------------
    install_order: list[str] = []  # The final result, built incrementally

    while ready_queue:
        # ---------------------------------------------------------------------
        # STEP 3a: Sort the queue alphabetically.
        # This enforces the "per-round alphabetical selection" constraint.
        # All currently-eligible packages are sorted before picking the next one.
        # ---------------------------------------------------------------------
        ready_queue.sort()

        # ---------------------------------------------------------------------
        # STEP 3b: Pop the first package (alphabetically smallest eligible one).
        # Using pop(0) on a list is O(N), acceptable here since the queue is
        # small. For very large graphs, a SortedList (from sortedcontainers)
        # would give O(log N) insertion + O(1) pop.
        # ---------------------------------------------------------------------
        current = ready_queue.pop(0)

        # ---------------------------------------------------------------------
        # STEP 3c: "Install" this package — add it to the result.
        # ---------------------------------------------------------------------
        install_order.append(current)

        # ---------------------------------------------------------------------
        # STEP 3d: For each package that was waiting on `current`, decrement
        # its in-degree. If it reaches 0, all its dependencies are now met:
        # add it to the queue so it becomes eligible in the next selection.
        # ---------------------------------------------------------------------
        for dependent in dependents[current]:
            in_degree[dependent] -= 1  # one fewer unresolved dependency
            if in_degree[dependent] == 0:
                # All dependencies of `dependent` are now installed
                ready_queue.append(dependent)

    # -------------------------------------------------------------------------
    # STEP 4: Cycle detection.
    # If install_order doesn't contain every package, some packages were never
    # added to the queue — meaning they always had at least one unresolved dep.
    # This only happens if there's a cycle (A depends on B, B depends on A).
    # -------------------------------------------------------------------------
    if len(install_order) != len(packages):
        # Find which packages were never resolved for a useful error message
        unresolved = set(packages.keys()) - set(install_order)
        raise ValueError(
            f"Cyclic dependency detected. Cannot resolve: {sorted(unresolved)}"
        )

    return install_order


# =============================================================================
# DEMONSTRATION
# =============================================================================

def print_section(title: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print('=' * 60)


if __name__ == "__main__":

    # -------------------------------------------------------------------------
    # Example 1: Simple linear chain
    # C <- B <- A  (A depends on B, B depends on C)
    # Only one valid order: C, B, A
    # -------------------------------------------------------------------------
    print_section("Example 1: Linear chain  A -> B -> C")
    chain = {
        "A": ["B"],
        "B": ["C"],
        "C": [],
    }
    result = resolve_dependencies(chain)
    print(f"Input:  {chain}")
    print(f"Order:  {result}")
    # Expected: ['C', 'B', 'A']

    # -------------------------------------------------------------------------
    # Example 2: Diamond dependency
    # D depends on B and C; both depend on A.
    # Round 1: [A] (only eligible)
    # Round 2: [B, C] (both become eligible, sorted alphabetically)
    # Round 3: [D]
    # -------------------------------------------------------------------------
    print_section("Example 2: Diamond  D -> B,C -> A")
    diamond = {
        "A": [],
        "B": ["A"],
        "C": ["A"],
        "D": ["B", "C"],
    }
    result = resolve_dependencies(diamond)
    print(f"Input:  {diamond}")
    print(f"Order:  {result}")
    # Expected: ['A', 'B', 'C', 'D']

    # -------------------------------------------------------------------------
    # Example 3: Alphabetical tie-breaking matters
    # Both 'zebra' and 'apple' depend on 'core'.
    # After 'core' is installed, 'apple' comes before 'zebra' alphabetically.
    # -------------------------------------------------------------------------
    print_section("Example 3: Alphabetical tie-breaking")
    tiebreak = {
        "zebra":  ["core"],
        "apple":  ["core"],
        "core":   [],
        "mango":  ["apple", "zebra"],
    }
    result = resolve_dependencies(tiebreak)
    print(f"Input:  {tiebreak}")
    print(f"Order:  {result}")
    # Expected: ['core', 'apple', 'zebra', 'mango']

    # -------------------------------------------------------------------------
    # Example 4: Realistic Python-like ecosystem
    # -------------------------------------------------------------------------
    print_section("Example 4: Realistic package ecosystem")
    ecosystem = {
        "flask":      ["werkzeug", "jinja2", "click"],
        "werkzeug":   [],
        "jinja2":     ["markupsafe"],
        "click":      [],
        "markupsafe": [],
        "requests":   ["urllib3", "certifi"],
        "urllib3":    [],
        "certifi":    [],
    }
    result = resolve_dependencies(ecosystem)
    print(f"Input packages: {sorted(ecosystem.keys())}")
    print(f"Install order:  {result}")
    # Expected: ['certifi', 'click', 'markupsafe', 'urllib3', 'werkzeug',
    #            'jinja2', 'requests', 'flask']

    # -------------------------------------------------------------------------
    # Example 5: Cycle detection
    # A -> B -> C -> A  (circular — unresolvable)
    # -------------------------------------------------------------------------
    print_section("Example 5: Cycle detection")
    cyclic = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"],  # cycle!
    }
    try:
        result = resolve_dependencies(cyclic)
    except ValueError as e:
        print(f"Caught expected error: {e}")

    # -------------------------------------------------------------------------
    # Example 6: Undeclared dependency detection
    # -------------------------------------------------------------------------
    print_section("Example 6: Undeclared dependency")
    bad_deps = {
        "A": ["ghost_package"],  # ghost_package is never declared
    }
    try:
        result = resolve_dependencies(bad_deps)
    except ValueError as e:
        print(f"Caught expected error: {e}")
