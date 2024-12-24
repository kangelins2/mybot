if std.extVar("env_slug") == "production" then [
  {
    apiVersion: 'bitnami.com/v1alpha1',
    kind: 'SealedSecret',
    metadata: {
      annotations: {
        'sealedsecrets.bitnami.com/namespace-wide': 'true',
      },
      name: 'token',
      namespace: 'ya-education-snake-backend-production',
    },
    spec: {
      encryptedData: {
        TG_BOT_TOKEN: 'AgBk586gb/mot1BnVJT7x+AF7uT+eNBizX0a4xylr+5CJ+AFXorpegv69582gDJdCx0THjwSl7G4xnWziSlh8wAX+NS8KVgaXFP9xu7FWxlqDS6qlERz+mznzpCyv4CtLeAq0htGorYQRSMD3hEMJ0qOqk91LmSs2F8ju5YvySmF074HK0a/v25HcghVwRbGEnCzaA3oVZCs/luP1nNse0LdK8WJuNh+iZ0vcu+oWgK+kSxEFQ60k5tErHIvj1NsDMIniXK8HOLJ7zvBozJMudLDfvgt+n5MkH1r0nO72fvQhCJ/qM9GeH8OwF/8VWFeqLnDGJ7WRvnpJEpUUqbH/R2wHyJqxFOxJhuszzPiT2FdqAQdx1sDS8VM+bgehlNfXJjYGloQdAyn9C6R8nuvm9X2x4GVRBW/0Q6WSSArvM3j0+KkJUwg+50pEnB8FFoxvMY9bc+okqgNhiP3XNpfo7UFfEa+7HrUPv1DHWsQVdkll3gi+esgMQlElhM1hwE1t1w8kKjpqtMahFT55I7wXfqrMAr4hnEUfDKglCSTmgHAntX8SusBnbuyCjO4erebuUj+TfBvxenU7vZ8y3VpHuTFhmNdevxHqAshGfCLOWEg8yagM7nM4qf/Q1+CIvGuzhhDrss/OdFqKjhkZLUiqwfpHoHhDpcNfT8Qbk6TkHCD71iZhwLtNu6i9Ek2BoN/DFk2jOxhGiyXF7YeGipb0eJqQhpH4LlNXGZBWuhk2Xp7nr4nA1fqZQcIn5bix/Lv',
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