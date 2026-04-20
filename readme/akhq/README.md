# AKHQ

## Issue with API docs

We should be able to access API docs through the `/api` endpoint; however, there is currently an issue with the image we are using (last version, 0.27.0) where the YAML file with the OpenAPI specs is not being distributed.

## Workaround for API docs

### Clone the source code

https://github.com/tchiotludo/akhq

Checkout the tag that corresponds to the version you are interested in. For instance, 0.27.0.

### Change `src/main/resources/application.yml`

Under `micronaut`, add:

```yaml
micronaut:
  openapi:
    enabled: true
    views:
      swagger-ui:
        enabled: true
        mapping: /swagger-ui
      rapidoc:
        enabled: true
        mapping: /rapidoc
```

### Build and find the file

```bash
./gradlew build -x test
```
_We do not care if tests fail at this point._

Then, find the file at: `build/classes/java/main/META-INF/swagger/akhq-1.0.0.yml`

### Pre-generated files

For convenience, find the files here as well:

- [0.27.0](0.27.0/api-docs.yaml)

### Pre-generated bruno collections

https://www.usebruno.com/

- [0.27.0](0.27.0/bruno/AKHQ/)