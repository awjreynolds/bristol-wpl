# Topology QA Rules

Status: Stage 4A control rules.  
Date: 2026-06-26.  
Owner: Spatial/Data Agent.

These rules define required future checks. They do not certify any boundary option.

## Boundary Geometry Checks

Each future boundary option must record:

- geometry validity;
- no self-intersections;
- no unintended gaps, overlaps or slivers;
- no duplicate features;
- correct CRS and transformation history;
- precision and tolerance settings;
- relationship to Bristol administrative boundary;
- islands and exclaves;
- road-centreline, railway, waterway or parcel-edge ambiguity;
- boundary-centred premises;
- cross-boundary sites;
- output hash for GeoPackage, GeoJSON and map products.

## Reconciliation Checks

The following must reconcile:

- GIS geometry;
- legal boundary wording;
- public map outputs;
- premises and parking spatial joins;
- boundary schedule;
- change log.

## Review Checks

Every check must have:

- boundary option ID;
- tool or reviewer;
- date;
- result;
- evidence reference;
- unresolved issue;
- reviewer status.

