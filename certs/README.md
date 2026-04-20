# Detailed mTLS configuration for Kafka brokers

## Approach

1. Create a custom Certificate Authority (CA).
1. Create certificates for each broker, signed by the custom CA.


## Certificate Authority (CA)

Create a private key for the CA.

```bash
openssl genrsa -out certs/ca/ca.key.pem 4096
```

Create a certificate for the CA using the private key.

```bash
openssl req -x509 -new -nodes -key certs/ca/ca.key.pem -sha256 -days 3650 -out certs/ca/ca.crt.pem -subj "/CN=ACME Certificate Authority"
```

## Private keys for each broker

```bash
openssl genrsa -out certs/kafka-1/kafka-1.key.pem 2048
```

```bash
openssl genrsa -out certs/kafka-2/kafka-2.key.pem 2048
```

```bash
openssl genrsa -out certs/kafka-3/kafka-3.key.pem 2048
```

## Certificate Signing Request (CSR)

This will create CSRs for each broker using their private keys and the CSR configuration files.

```bash
openssl req -new -key certs/kafka-1/kafka-1.key.pem -out certs/kafka-1/kafka-1.csr.pem -config certs/kafka-1/openssl.cnf
```

```bash
openssl req -new -key certs/kafka-2/kafka-2.key.pem -out certs/kafka-2/kafka-2.csr.pem -config certs/kafka-2/openssl.cnf
```

```bash
openssl req -new -key certs/kafka-3/kafka-3.key.pem -out certs/kafka-3/kafka-3.csr.pem -config certs/kafka-3/openssl.cnf
```

## Certificates for each broker

Notice that the openssl.cnf file is being used again because it contains a `[ v3_req ]` section, which is relevant to issue the certificate.

```bash
openssl x509 -req -in certs/kafka-1/kafka-1.csr.pem \
  -CA certs/ca/ca.crt.pem \
  -CAkey certs/ca/ca.key.pem \
  -CAcreateserial \
  -out certs/kafka-1/kafka-1.crt.pem -days 365 \
  -sha256 -extensions v3_req \
  -extfile certs/kafka-1/openssl.cnf
```

```bash
openssl x509 -req -in certs/kafka-2/kafka-2.csr.pem \
  -CA certs/ca/ca.crt.pem \
  -CAkey certs/ca/ca.key.pem \
  -CAcreateserial \
  -out certs/kafka-2/kafka-2.crt.pem -days 365 \
  -sha256 -extensions v3_req \
  -extfile certs/kafka-2/openssl.cnf
```

```bash
openssl x509 -req -in certs/kafka-3/kafka-3.csr.pem \
  -CA certs/ca/ca.crt.pem \
  -CAkey certs/ca/ca.key.pem \
  -CAcreateserial \
  -out certs/kafka-3/kafka-3.crt.pem -days 365 \
  -sha256 -extensions v3_req \
  -extfile certs/kafka-3/openssl.cnf  
```

## PKCS#12 stores for each broker

These files will combine the private key, the certificate chain (including the CA cert), and the certificate for each broker in a convenient bundle.

```bash
openssl pkcs12 -export \
  -in certs/kafka-1/kafka-1.crt.pem \
  -inkey certs/kafka-1/kafka-1.key.pem \
  -chain -CAfile certs/ca/ca.crt.pem \
  -name kafka-1 \
  -passout pass:brokerpass \
  -out certs/kafka-1/kafka-1.keystore.p12
```

```bash
openssl pkcs12 -export \
  -in certs/kafka-2/kafka-2.crt.pem \
  -inkey certs/kafka-2/kafka-2.key.pem \
  -chain -CAfile certs/ca/ca.crt.pem \
  -name kafka-2 \
  -passout pass:brokerpass \
  -out certs/kafka-2/kafka-2.keystore.p12
```

```bash
openssl pkcs12 -export \
  -in certs/kafka-3/kafka-3.crt.pem \
  -inkey certs/kafka-3/kafka-3.key.pem \
  -chain -CAfile certs/ca/ca.crt.pem \
  -name kafka-3 \
  -passout pass:brokerpass \
  -out certs/kafka-3/kafka-3.keystore.p12
```

## Java truststore for each broker

```bash
keytool -importcert -trustcacerts -alias CARoot \
  -file certs/ca/ca.crt.pem \
  -keystore certs/kafka-1/kafka.truststore.p12 \
  -storetype PKCS12 -storepass brokerpass -noprompt
```

```bash
keytool -importcert -trustcacerts -alias CARoot \
  -file certs/ca/ca.crt.pem \
  -keystore certs/kafka-2/kafka.truststore.p12 \
  -storetype PKCS12 -storepass brokerpass -noprompt
```

```bash
keytool -importcert -trustcacerts -alias CARoot \
  -file certs/ca/ca.crt.pem \
  -keystore certs/kafka-3/kafka.truststore.p12 \
  -storetype PKCS12 -storepass brokerpass -noprompt
```

Step-by-step
- `keytool` Run the Java key management utility.
- `-importcert` Import a certificate into a keystore/truststore.
- `-trustcacerts` Treat the imported cert as a trusted CA certificate. This makes the store a truststore instead of a regular identity keystore.
- `-alias CARoot` Give the imported certificate the name CARoot inside the store. The alias is how the cert is identified later.
- `-file certs/ca/ca.crt.pem` Read the certificate to import from this file.
- `-keystore certs/kafka-1/kafka.truststore.p12` Write the result into this PKCS#12 store file. This is the broker truststore used by Kafka to verify client certs or peer certs.
- `-storetype PKCS12` Use the PKCS#12 file format for the store.
That makes it compatible with Kafka’s SSL configuration.
- `-storepass brokerpass` Protect the store with the password brokerpass. Kafka will need this password to open the truststore.
- `-noprompt` Don’t ask for confirmation before importing. The import happens non-interactively.

## Client Certificates

To connect clients securely via mTLS, you need to create and sign client certificates using the same CA.

### Creating a Client Certificate

1. Generate a private key for the client:
   ```bash
   openssl genrsa -out certs/client/client.key.pem 2048
   ```

2. Create a CSR for the client (update `certs/client/openssl.cnf` with client-specific details):
   ```bash
   openssl req -new -key certs/client/client.key.pem -out certs/client/client.csr.pem -config certs/client/openssl.cnf
   ```

3. Sign the CSR with your CA:
   ```bash
   openssl x509 -req -in certs/client/client.csr.pem \
     -CA certs/ca/ca.crt.pem -CAkey certs/ca/ca.key.pem -CAcreateserial \
     -out certs/client/client.crt.pem -days 365 \
     -sha256 -extensions v3_req -extfile certs/client/openssl.cnf
   ```

4. Create a PKCS#12 keystore for the client:
   ```bash
   openssl pkcs12 -export \
     -in certs/client/client.crt.pem \
     -inkey certs/client/client.key.pem \
     -chain -CAfile certs/ca/ca.crt.pem \
     -name client \
     -passout pass:clientpass \
     -out certs/client/client.keystore.p12
   ```

5. Create a truststore for the client (containing the CA cert):
   ```bash
   keytool -importcert -trustcacerts -alias CARoot \
     -file certs/ca/ca.crt.pem \
     -keystore certs/client/client.truststore.p12 \
     -storetype PKCS12 -storepass clientpass -noprompt
   ```

### How Kafka Trusts Client Certificates

Kafka brokers automatically trust any client certificate that is:
- Signed by the CA whose certificate is in the broker's truststore (`kafka.truststore.p12`).
- Valid (not expired, not revoked).
- Presented during the mTLS handshake.

Since `ssl.client.auth=required` is set, clients must provide a valid certificate. If the cert is signed by your CA, the broker accepts it as authenticated.

### Restricting Access with ACLs

To control which authenticated clients can access specific resources (topics, etc.), use Kafka ACLs. ACLs work with the "principal" extracted from the client certificate (e.g., the CN field).

1. Issue client certificates with unique CNs (e.g., `CN=producer-app`, `CN=consumer-app`).

2. Use `kafka-acls` to set permissions based on the principal:
   ```bash
   # Allow producer-app to write to a topic
   kafka-acls --bootstrap-server localhost:9097 --command-config admin.properties --add --allow-principal User:producer-app --operation Write --topic my-topic

   # Allow consumer-app to read from a topic
   kafka-acls --bootstrap-server localhost:9097 --command-config admin.properties --add --allow-principal User:consumer-app --operation Read --topic my-topic
   ```

This way, even if multiple clients have valid certificates from the CA, only those with matching ACLs can perform operations.

For production, consider using Certificate Revocation Lists (CRLs) to revoke specific certificates if needed.