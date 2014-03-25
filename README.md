Dart Skeleton Project
=====================

This is a skeleton project to use dart with a `waf` build script. It provides
rudimentary support for dart web projects in waf via the `dart2js` script and
`dart.js` bootstrapping file. Add source files (dart, html, css, js) under
'src'. Doesn't handle server-side dart, that can come later...

Notes on Dart Project Structure
-------------------------------

`dart2js` compiles applications, not libraries; i.e. if you have import
statements or part statements in your used files, you only call `dart2js`
once on the root file (typically the one with `main`).

The files in `/tools/` shouldn't need to be changed. They set up the `waf`
tool such that it can handle dart files.

The `packages` directory is treated as the Dart packages root. This is set by
the wscript file in that directory via the environment variable `PACKAGES`.

Due to the interpreted nature of Dart, use variables and related things don't
really need to be handled.

Depending on how you want to roll, you can either drop dart packages into the
`/packages/` folder, or specify them in `pubspec.yaml` and use `pub`. Indicate
to the rest of the system your choice in `/wscript`. You may also want to
update `/.gitignore` to include `packages/*` if you use `pub`, so that
automatically handled dependencies aren't added to the versioning system.

