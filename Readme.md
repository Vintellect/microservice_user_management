# User Management

This service is responsible for handling user-related operations within our infrastructure.

## Deployment Instructions

To deploy the User Management service, start by copying the example application configuration:

```sh
cp example.app.yml app.yml
```

Next, you need to update the following variables in the `.env` file:

```yml
SPANNER_INSTANCE: "YOUR-SPANNER_INSTANCE"
SPANNER_DATABASE: "YOUR-USER-DATABASE"
```

Replace the placeholders (`YOUR-SPANNER_INSTANCE`, and `YOUR-USER-DATABASE`) with your Spanner instance name, and Spanner database name, respectively.

For a more comprehensive guide on deployment, including detailed steps and additional configurations, please refer to our [App Engine Deployment Guide](https://github.com/Vintellect/deploy_backend_guide/blob/fd5863fb17d5386cdf16eb43cf58b0c6b8cc571f/Microserivces_guide.md).