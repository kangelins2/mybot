if std.extVar("env_slug") == "staging" then [
  {
    apiVersion: 'bitnami.com/v1alpha1',
    kind: 'SealedSecret',
    metadata: {
      annotations: {
        'sealedsecrets.bitnami.com/namespace-wide': 'true',
      },
      name: 'token',
    },
    spec: {
      encryptedData: {
        TG_BOT_TOKEN: 'AgAuWSioNOb2XTX6lMHEJmW/lABT5I3/uOxKJ9pK+jo66GuWbzlPVgcZjrS4sLKm6r5JGFq9c1Uyn5w+iACyAXJrtz7R5EVrI5ZrZFPVI5q5o3zS1UulpaxtYtS2EfMxWEjg5RJGjJQtezkpO85/JpeYcF9ORb3lfC0c/zdet0qNE0HFoh+QX/HtVaZj7YO6jDK01c8aQ0Inf6lgSCJ5y83vP+p6VQgruz1qVj5TXWpyX0FPwojGNd3vjQiElCEhvsrib/WVfXY03FjaHCpJmaIuhM8422cmNio7H9UeaNUH4EOq2itiw9OUv6H/NNXmFaQbh90r3D9OfaEXifxgI/kqVQVuXLYb9Vd90pHGtCZdk0ctdruQ0NG8xdAWtnCWpO7QE1RuICjIUCMfTFYKaRAM0yH8ckw+NMffakkSW+t6R19f9RLS8AMhQ5lzM1KrtFLlSzuM5xdNIREaNd7F95VIXrfGMV/8sEb4Xi53CEKcFudRWiKBlhkcUlVFOXyK8be63YuZvhBv1HuZmAichZSQVy89qZW6bPfCSs6HNiw5rsbi1M2pT+qdXFPK3dg95VGrNDjpWbuoVWx2dwZOHrIQT/rjHebGT7Icjqms9eoHc+EynqTFUE9sTjSSGX6zm+9NSQtQTAMU9c7hYgm8dq2rmWBI9EsM1D+gTH5f4ujnqz8CqRxJDs7E2sPuVqdfWSGSFDi5jrhnyJJjqpJnGu48FZ8xmbY7sd3S96lyDsmqhsZ4x8pZ2E/OX2HTTYM5',
      },
      template: {
        metadata: {
          annotations: {
            'sealedsecrets.bitnami.com/namespace-wide': 'true',
          },
          name: 'token',
        },
        type: 'Opaque',
      },
    },
  },
]