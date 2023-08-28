# Getting Started with DataHarmonizer

This project was bootstrapped with `create-data-harmonizer`.

## Available Scripts

In the project directory, you can run:

### `npm run dev`

Runs the app in the development mode.
Open [http://localhost:5173](http://localhost:5173) to view it in your browser.

### `npm run build`

Builds the app for production to the `dist` folder. This directory can be deployed to any static hosting service, such as [GitHub Pages](https://docs.github.com/en/pages/quickstart).

### `npm run preview`

Previews the production build locally.

### `npm run update-schema`

Reloads the same schema that was used to bootstrap the project into the `schemas` directory. 

## Schema Management

This project depends on [linkml-runtime.js](https://github.com/linkml/linkml-runtime.js), which provides a command line executable, `gen-linkml`, for converting YAML LinkML schemas into the JSON format required by DataHarmonizer. This executable is used by the `update-schema` script. It can also be used in a one-off fashion to add additional schemas. When `gen-linkml` is used to add or update schemas, you may need to manually update `menu.json` to keep it in sync with the new schemas and/or class names.
