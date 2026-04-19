# Kafka Introspection Report

## Cluster

- **Cluster ID:** `5L6g3nShT-eMCtK--X86sw`
- **Controller ID:** `2`
- **Bootstrap servers:** `localhost:9094, localhost:9095, localhost:9096`

## Brokers

| node_id | host | port | rack |
| --- | --- | --- | --- |
| 3 | localhost | 9096 |  |
| 1 | localhost | 9094 |  |
| 2 | localhost | 9095 |  |

## Topics

### `Accounts`

| partition | leader | replicas | isr |
| --- | --- | --- | --- |
| 0 | 3 | 3, 1, 2 | 1, 2, 3 |
| 1 | 1 | 1, 2, 3 | 1, 2, 3 |
| 2 | 2 | 2, 3, 1 | 1, 2, 3 |

## Broker Configs

### Broker `1`

| name | value | source | default | readonly | sensitive |
| --- | --- | --- | --- | --- | --- |
| add.partitions.to.txn.retry.backoff.max.ms | 100 | 5 | false | true | false |
| add.partitions.to.txn.retry.backoff.ms | 20 | 5 | false | true | false |
| advertised.listeners | DOCKER://kafka-1:9092,HOST://localhost:9094 | 4 | false | true | false |
| allow.plaintext.listener |  | 4 | false | true | true |
| alter.config.policy.class.name |  | 5 | false | true | false |
| alter.log.dirs.replication.quota.window.num | 11 | 5 | false | true | false |
| alter.log.dirs.replication.quota.window.size.seconds | 1 | 5 | false | true | false |
| authorizer.class.name |  | 5 | false | true | false |
| auto.create.topics.enable | false | 4 | false | true | false |
| auto.leader.rebalance.enable | true | 5 | false | true | false |
| background.threads | 10 | 5 | false | false | false |
| broker.heartbeat.interval.ms | 2000 | 5 | false | true | false |
| broker.id | 1 | 4 | false | true | false |
| broker.rack |  | 5 | false | true | false |
| broker.session.timeout.ms | 9000 | 5 | false | true | false |
| client.quota.callback.class |  | 5 | false | true | false |
| cluster.id |  | 4 | false | true | true |
| compression.gzip.level | -1 | 5 | false | false | false |
| compression.lz4.level | 9 | 5 | false | false | false |
| compression.type | producer | 5 | false | false | false |
| compression.zstd.level | 3 | 5 | false | false | false |
| config.providers |  | 5 | false | false | false |
| connection.failed.authentication.delay.ms | 100 | 5 | false | true | false |
| connections.max.idle.ms | 600000 | 5 | false | true | false |
| connections.max.reauth.ms | 0 | 5 | false | true | false |
| controlled.shutdown.enable | true | 5 | false | true | false |
| controller.listener.names | CONTROLLER | 4 | false | true | false |
| controller.quorum.append.linger.ms | 25 | 5 | false | true | false |
| controller.quorum.auto.join.enable | false | 5 | false | true | false |
| controller.quorum.bootstrap.servers |  | 5 | false | true | false |
| controller.quorum.election.backoff.max.ms | 1000 | 5 | false | true | false |
| controller.quorum.election.timeout.ms | 1000 | 5 | false | true | false |
| controller.quorum.fetch.timeout.ms | 2000 | 5 | false | true | false |
| controller.quorum.request.timeout.ms | 2000 | 5 | false | true | false |
| controller.quorum.retry.backoff.ms | 20 | 5 | false | true | false |
| controller.quorum.voters | 1@kafka-1:9093,2@kafka-2:9093,3@kafka-3:9093 | 4 | false | true | false |
| controller.quota.window.num | 11 | 5 | false | true | false |
| controller.quota.window.size.seconds | 1 | 5 | false | true | false |
| controller.socket.timeout.ms | 30000 | 5 | false | true | false |
| create.topic.policy.class.name |  | 5 | false | true | false |
| default.replication.factor | 3 | 4 | false | true | false |
| delegation.token.expiry.check.interval.ms | 3600000 | 5 | false | true | false |
| delegation.token.expiry.time.ms | 86400000 | 5 | false | true | false |
| delegation.token.max.lifetime.ms | 604800000 | 5 | false | true | false |
| delegation.token.secret.key |  | 5 | false | true | true |
| delete.records.purgatory.purge.interval.requests | 1 | 5 | false | true | false |
| delete.topic.enable | true | 5 | false | true | false |
| early.start.listeners |  | 5 | false | true | false |
| fetch.max.bytes | 57671680 | 5 | false | true | false |
| fetch.purgatory.purge.interval.requests | 1000 | 5 | false | true | false |
| group.consumer.assignors | uniform,range | 5 | false | true | false |
| group.consumer.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.consumer.max.heartbeat.interval.ms | 15000 | 5 | false | true | false |
| group.consumer.max.session.timeout.ms | 60000 | 5 | false | true | false |
| group.consumer.max.size | 2147483647 | 5 | false | true | false |
| group.consumer.migration.policy | bidirectional | 5 | false | true | false |
| group.consumer.min.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.consumer.min.session.timeout.ms | 45000 | 5 | false | true | false |
| group.consumer.session.timeout.ms | 45000 | 5 | false | true | false |
| group.coordinator.append.linger.ms | -1 | 5 | false | true | false |
| group.coordinator.rebalance.protocols | classic,consumer,streams | 5 | false | true | false |
| group.coordinator.threads | 4 | 5 | false | true | false |
| group.initial.rebalance.delay.ms | 3000 | 5 | false | true | false |
| group.max.session.timeout.ms | 1800000 | 5 | false | true | false |
| group.max.size | 2147483647 | 5 | false | true | false |
| group.min.session.timeout.ms | 6000 | 5 | false | true | false |
| group.share.assignors | simple | 5 | false | true | false |
| group.share.delivery.count.limit | 5 | 5 | false | true | false |
| group.share.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.share.max.heartbeat.interval.ms | 15000 | 5 | false | true | false |
| group.share.max.record.lock.duration.ms | 60000 | 5 | false | true | false |
| group.share.max.session.timeout.ms | 60000 | 5 | false | true | false |
| group.share.max.share.sessions | 2000 | 5 | false | true | false |
| group.share.max.size | 200 | 5 | false | true | false |
| group.share.min.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.share.min.record.lock.duration.ms | 15000 | 5 | false | true | false |
| group.share.min.session.timeout.ms | 45000 | 5 | false | true | false |
| group.share.partition.max.record.locks | 2000 | 5 | false | true | false |
| group.share.record.lock.duration.ms | 30000 | 5 | false | true | false |
| group.share.session.timeout.ms | 45000 | 5 | false | true | false |
| group.streams.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.streams.initial.rebalance.delay.ms | 3000 | 5 | false | true | false |
| group.streams.max.heartbeat.interval.ms | 15000 | 5 | false | true | false |
| group.streams.max.session.timeout.ms | 60000 | 5 | false | true | false |
| group.streams.max.size | 2147483647 | 5 | false | true | false |
| group.streams.max.standby.replicas | 2 | 5 | false | true | false |
| group.streams.min.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.streams.min.session.timeout.ms | 45000 | 5 | false | true | false |
| group.streams.num.standby.replicas | 0 | 5 | false | true | false |
| group.streams.session.timeout.ms | 45000 | 5 | false | true | false |
| initial.broker.registration.timeout.ms | 60000 | 5 | false | true | false |
| inter.broker.listener.name | DOCKER | 4 | false | true | false |
| kafka.metrics.polling.interval.secs | 10 | 5 | false | true | false |
| kafka.metrics.reporters |  | 5 | false | true | false |
| leader.imbalance.check.interval.seconds | 300 | 5 | false | true | false |
| listener.security.protocol.map | CONTROLLER:PLAINTEXT,DOCKER:PLAINTEXT,HOST:PLAINTEXT | 4 | false | false | false |
| listeners | DOCKER://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093,HOST://0.0.0.0:9094 | 4 | false | false | false |
| log.cleaner.backoff.ms | 15000 | 5 | false | false | false |
| log.cleaner.dedupe.buffer.size | 134217728 | 5 | false | false | false |
| log.cleaner.delete.retention.ms | 86400000 | 5 | false | false | false |
| log.cleaner.enable | true | 5 | false | true | false |
| log.cleaner.io.buffer.load.factor | 0.9 | 5 | false | false | false |
| log.cleaner.io.buffer.size | 524288 | 5 | false | false | false |
| log.cleaner.io.max.bytes.per.second | 1.7976931348623157E308 | 5 | false | false | false |
| log.cleaner.max.compaction.lag.ms | 9223372036854775807 | 5 | false | false | false |
| log.cleaner.min.cleanable.ratio | 0.5 | 5 | false | false | false |
| log.cleaner.min.compaction.lag.ms | 0 | 5 | false | false | false |
| log.cleaner.threads | 1 | 5 | false | false | false |
| log.cleanup.policy | delete | 5 | false | false | false |
| log.dir | /tmp/kafka-logs | 5 | false | true | false |
| log.dir.failure.timeout.ms | 30000 | 5 | false | true | false |
| log.dirs |  | 5 | false | true | false |
| log.flush.interval.messages | 9223372036854775807 | 5 | false | false | false |
| log.flush.interval.ms |  | 5 | false | false | false |
| log.flush.offset.checkpoint.interval.ms | 60000 | 5 | false | true | false |
| log.flush.scheduler.interval.ms | 9223372036854775807 | 5 | false | true | false |
| log.flush.start.offset.checkpoint.interval.ms | 60000 | 5 | false | true | false |
| log.index.interval.bytes | 4096 | 5 | false | false | false |
| log.index.size.max.bytes | 10485760 | 5 | false | false | false |
| log.local.retention.bytes | -2 | 5 | false | false | false |
| log.local.retention.ms | -2 | 5 | false | false | false |
| log.message.timestamp.after.max.ms | 3600000 | 5 | false | false | false |
| log.message.timestamp.before.max.ms | 9223372036854775807 | 5 | false | false | false |
| log.message.timestamp.type | CreateTime | 5 | false | false | false |
| log.preallocate | false | 5 | false | false | false |
| log.retention.bytes | -1 | 5 | false | false | false |
| log.retention.check.interval.ms | 300000 | 5 | false | true | false |
| log.retention.hours | 168 | 5 | false | true | false |
| log.retention.minutes |  | 5 | false | true | false |
| log.retention.ms |  | 5 | false | false | false |
| log.roll.hours | 168 | 5 | false | true | false |
| log.roll.jitter.hours | 0 | 5 | false | true | false |
| log.roll.jitter.ms |  | 5 | false | false | false |
| log.roll.ms |  | 5 | false | false | false |
| log.segment.bytes | 1073741824 | 5 | false | false | false |
| log.segment.delete.delay.ms | 60000 | 5 | false | false | false |
| max.connection.creation.rate | 2147483647 | 5 | false | false | false |
| max.connections | 2147483647 | 5 | false | false | false |
| max.connections.per.ip | 2147483647 | 5 | false | false | false |
| max.connections.per.ip.overrides |  | 5 | false | false | false |
| max.incremental.fetch.session.cache.slots | 1000 | 5 | false | true | false |
| max.request.partition.size.limit | 2000 | 5 | false | true | false |
| message.max.bytes | 1048588 | 5 | false | false | false |
| metadata.log.dir |  | 5 | false | true | false |
| metadata.log.max.record.bytes.between.snapshots | 20971520 | 5 | false | true | false |
| metadata.log.max.snapshot.interval.ms | 3600000 | 5 | false | true | false |
| metadata.log.segment.bytes | 1073741824 | 5 | false | true | false |
| metadata.log.segment.ms | 604800000 | 5 | false | true | false |
| metadata.max.idle.interval.ms | 500 | 5 | false | true | false |
| metadata.max.retention.bytes | 104857600 | 5 | false | true | false |
| metadata.max.retention.ms | 604800000 | 5 | false | true | false |
| metric.reporters | org.apache.kafka.common.metrics.JmxReporter | 5 | false | false | false |
| metrics.num.samples | 2 | 5 | false | true | false |
| metrics.recording.level | INFO | 5 | false | true | false |
| metrics.sample.window.ms | 30000 | 5 | false | true | false |
| min.insync.replicas | 2 | 3 | false | false | false |
| node.id | 1 | 4 | false | true | false |
| num.io.threads | 8 | 5 | false | false | false |
| num.network.threads | 3 | 5 | false | false | false |
| num.partitions | 1 | 5 | false | true | false |
| num.recovery.threads.per.data.dir | 2 | 5 | false | false | false |
| num.replica.alter.log.dirs.threads |  | 5 | false | true | false |
| num.replica.fetchers | 1 | 5 | false | false | false |
| offset.metadata.max.bytes | 4096 | 5 | false | true | false |
| offsets.commit.timeout.ms | 5000 | 5 | false | true | false |
| offsets.load.buffer.size | 5242880 | 5 | false | true | false |
| offsets.retention.check.interval.ms | 600000 | 5 | false | true | false |
| offsets.retention.minutes | 10080 | 5 | false | true | false |
| offsets.topic.compression.codec | 0 | 5 | false | true | false |
| offsets.topic.num.partitions | 50 | 5 | false | true | false |
| offsets.topic.replication.factor | 3 | 4 | false | true | false |
| offsets.topic.segment.bytes | 104857600 | 5 | false | true | false |
| principal.builder.class | org.apache.kafka.common.security.authenticator.DefaultKafkaPrincipalBuilder | 5 | false | false | false |
| process.roles | broker,controller | 4 | false | true | false |
| producer.id.expiration.ms | 86400000 | 5 | false | false | false |
| producer.purgatory.purge.interval.requests | 1000 | 5 | false | true | false |
| queued.max.request.bytes | -1 | 5 | false | true | false |
| queued.max.requests | 500 | 5 | false | true | false |
| quota.window.num | 11 | 5 | false | true | false |
| quota.window.size.seconds | 1 | 5 | false | true | false |
| remote.fetch.max.wait.ms | 500 | 5 | false | false | false |
| remote.list.offsets.request.timeout.ms | 30000 | 5 | false | false | false |
| remote.log.index.file.cache.total.size.bytes | 1073741824 | 5 | false | false | false |
| remote.log.manager.copier.thread.pool.size | 10 | 5 | false | false | false |
| remote.log.manager.copy.max.bytes.per.second | 9223372036854775807 | 5 | false | false | false |
| remote.log.manager.copy.quota.window.num | 11 | 5 | false | true | false |
| remote.log.manager.copy.quota.window.size.seconds | 1 | 5 | false | true | false |
| remote.log.manager.expiration.thread.pool.size | 10 | 5 | false | false | false |
| remote.log.manager.fetch.max.bytes.per.second | 9223372036854775807 | 5 | false | false | false |
| remote.log.manager.fetch.quota.window.num | 11 | 5 | false | true | false |
| remote.log.manager.fetch.quota.window.size.seconds | 1 | 5 | false | true | false |
| remote.log.manager.follower.thread.pool.size | 2 | 5 | false | false | false |
| remote.log.manager.task.interval.ms | 30000 | 5 | false | true | false |
| remote.log.manager.thread.pool.size | 2 | 5 | false | true | false |
| remote.log.metadata.custom.metadata.max.bytes | 128 | 5 | false | true | false |
| remote.log.metadata.manager.class.name | org.apache.kafka.server.log.remote.metadata.storage.TopicBasedRemoteLogMetadataManager | 5 | false | true | false |
| remote.log.metadata.manager.class.path |  | 5 | false | true | false |
| remote.log.metadata.manager.impl.prefix | rlmm.config. | 5 | false | true | false |
| remote.log.metadata.manager.listener.name |  | 5 | false | true | false |
| remote.log.reader.max.pending.tasks | 100 | 5 | false | true | false |
| remote.log.reader.threads | 10 | 5 | false | false | false |
| remote.log.storage.manager.class.name |  | 5 | false | true | false |
| remote.log.storage.manager.class.path |  | 5 | false | true | false |
| remote.log.storage.manager.impl.prefix | rsm.config. | 5 | false | true | false |
| remote.log.storage.system.enable | false | 5 | false | true | false |
| replica.fetch.backoff.ms | 1000 | 5 | false | true | false |
| replica.fetch.max.bytes | 1048576 | 5 | false | true | false |
| replica.fetch.min.bytes | 1 | 5 | false | true | false |
| replica.fetch.response.max.bytes | 10485760 | 5 | false | true | false |
| replica.fetch.wait.max.ms | 500 | 5 | false | true | false |
| replica.high.watermark.checkpoint.interval.ms | 5000 | 5 | false | true | false |
| replica.lag.time.max.ms | 30000 | 5 | false | true | false |
| replica.selector.class |  | 5 | false | true | false |
| replica.socket.receive.buffer.bytes | 65536 | 5 | false | true | false |
| replica.socket.timeout.ms | 30000 | 5 | false | true | false |
| replication.quota.window.num | 11 | 5 | false | true | false |
| replication.quota.window.size.seconds | 1 | 5 | false | true | false |
| request.timeout.ms | 30000 | 5 | false | true | false |
| sasl.client.callback.handler.class |  | 5 | false | true | false |
| sasl.enabled.mechanisms | GSSAPI | 5 | false | false | false |
| sasl.jaas.config |  | 5 | false | false | true |
| sasl.kerberos.kinit.cmd | /usr/bin/kinit | 5 | false | false | false |
| sasl.kerberos.min.time.before.relogin | 60000 | 5 | false | false | false |
| sasl.kerberos.principal.to.local.rules | DEFAULT | 5 | false | false | false |
| sasl.kerberos.service.name |  | 5 | false | false | false |
| sasl.kerberos.ticket.renew.jitter | 0.05 | 5 | false | false | false |
| sasl.kerberos.ticket.renew.window.factor | 0.8 | 5 | false | false | false |
| sasl.login.callback.handler.class |  | 5 | false | true | false |
| sasl.login.class |  | 5 | false | true | false |
| sasl.login.connect.timeout.ms |  | 5 | false | true | false |
| sasl.login.read.timeout.ms |  | 5 | false | true | false |
| sasl.login.refresh.buffer.seconds | 300 | 5 | false | false | false |
| sasl.login.refresh.min.period.seconds | 60 | 5 | false | false | false |
| sasl.login.refresh.window.factor | 0.8 | 5 | false | false | false |
| sasl.login.refresh.window.jitter | 0.05 | 5 | false | false | false |
| sasl.login.retry.backoff.max.ms | 10000 | 5 | false | true | false |
| sasl.login.retry.backoff.ms | 100 | 5 | false | true | false |
| sasl.mechanism.controller.protocol | GSSAPI | 5 | false | true | false |
| sasl.mechanism.inter.broker.protocol | GSSAPI | 5 | false | false | false |
| sasl.oauthbearer.assertion.algorithm | RS256 | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.aud |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.exp.seconds | 300 | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.iss |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.jti.include | false | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.nbf.seconds | 60 | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.sub |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.file |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.private.key.file |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.private.key.passphrase |  | 5 | false | true | true |
| sasl.oauthbearer.assertion.template.file |  | 5 | false | true | false |
| sasl.oauthbearer.client.credentials.client.id |  | 5 | false | true | false |
| sasl.oauthbearer.client.credentials.client.secret |  | 5 | false | true | true |
| sasl.oauthbearer.clock.skew.seconds | 30 | 5 | false | true | false |
| sasl.oauthbearer.expected.audience |  | 5 | false | true | false |
| sasl.oauthbearer.expected.issuer |  | 5 | false | true | false |
| sasl.oauthbearer.jwks.endpoint.refresh.ms | 3600000 | 5 | false | true | false |
| sasl.oauthbearer.jwks.endpoint.retry.backoff.max.ms | 10000 | 5 | false | true | false |
| sasl.oauthbearer.jwks.endpoint.retry.backoff.ms | 100 | 5 | false | true | false |
| sasl.oauthbearer.jwks.endpoint.url |  | 5 | false | true | false |
| sasl.oauthbearer.jwt.retriever.class | org.apache.kafka.common.security.oauthbearer.DefaultJwtRetriever | 5 | false | true | false |
| sasl.oauthbearer.jwt.validator.class | org.apache.kafka.common.security.oauthbearer.DefaultJwtValidator | 5 | false | true | false |
| sasl.oauthbearer.scope |  | 5 | false | true | false |
| sasl.oauthbearer.scope.claim.name | scope | 5 | false | true | false |
| sasl.oauthbearer.sub.claim.name | sub | 5 | false | true | false |
| sasl.oauthbearer.token.endpoint.url |  | 5 | false | true | false |
| sasl.server.callback.handler.class |  | 5 | false | true | false |
| sasl.server.max.receive.size | 524288 | 5 | false | true | false |
| security.inter.broker.protocol | PLAINTEXT | 5 | false | true | false |
| security.providers |  | 5 | false | true | false |
| share.coordinator.append.linger.ms | -1 | 5 | false | true | false |
| share.coordinator.load.buffer.size | 5242880 | 5 | false | true | false |
| share.coordinator.snapshot.update.records.per.snapshot | 500 | 5 | false | true | false |
| share.coordinator.state.topic.compression.codec | 0 | 5 | false | true | false |
| share.coordinator.state.topic.min.isr | 2 | 5 | false | true | false |
| share.coordinator.state.topic.num.partitions | 50 | 5 | false | true | false |
| share.coordinator.state.topic.replication.factor | 3 | 5 | false | true | false |
| share.coordinator.state.topic.segment.bytes | 104857600 | 5 | false | true | false |
| share.coordinator.threads | 1 | 5 | false | true | false |
| share.coordinator.write.timeout.ms | 5000 | 5 | false | true | false |
| share.fetch.purgatory.purge.interval.requests | 1000 | 5 | false | true | false |
| socket.connection.setup.timeout.max.ms | 30000 | 5 | false | true | false |
| socket.connection.setup.timeout.ms | 10000 | 5 | false | true | false |
| socket.listen.backlog.size | 50 | 5 | false | true | false |
| socket.receive.buffer.bytes | 102400 | 5 | false | true | false |
| socket.request.max.bytes | 104857600 | 5 | false | true | false |
| socket.send.buffer.bytes | 102400 | 5 | false | true | false |
| ssl.allow.dn.changes | false | 5 | false | true | false |
| ssl.allow.san.changes | false | 5 | false | true | false |
| ssl.cipher.suites |  | 5 | false | false | false |
| ssl.client.auth | none | 5 | false | false | false |
| ssl.enabled.protocols | TLSv1.2,TLSv1.3 | 5 | false | false | false |
| ssl.endpoint.identification.algorithm | https | 5 | false | false | false |
| ssl.engine.factory.class |  | 5 | false | false | false |
| ssl.key.password |  | 5 | false | false | true |
| ssl.keymanager.algorithm | SunX509 | 5 | false | false | false |
| ssl.keystore.certificate.chain |  | 5 | false | false | true |
| ssl.keystore.key |  | 5 | false | false | true |
| ssl.keystore.location |  | 5 | false | false | false |
| ssl.keystore.password |  | 5 | false | false | true |
| ssl.keystore.type | JKS | 5 | false | false | false |
| ssl.principal.mapping.rules | DEFAULT | 5 | false | true | false |
| ssl.protocol | TLSv1.3 | 5 | false | false | false |
| ssl.provider |  | 5 | false | false | false |
| ssl.secure.random.implementation |  | 5 | false | false | false |
| ssl.trustmanager.algorithm | PKIX | 5 | false | false | false |
| ssl.truststore.certificates |  | 5 | false | false | true |
| ssl.truststore.location |  | 5 | false | false | false |
| ssl.truststore.password |  | 5 | false | false | true |
| ssl.truststore.type | JKS | 5 | false | false | false |
| telemetry.max.bytes | 1048576 | 5 | false | true | false |
| transaction.abort.timed.out.transaction.cleanup.interval.ms | 10000 | 5 | false | true | false |
| transaction.max.timeout.ms | 900000 | 5 | false | true | false |
| transaction.partition.verification.enable | true | 5 | false | false | false |
| transaction.remove.expired.transaction.cleanup.interval.ms | 3600000 | 5 | false | true | false |
| transaction.state.log.load.buffer.size | 5242880 | 5 | false | true | false |
| transaction.state.log.min.isr | 2 | 4 | false | true | false |
| transaction.state.log.num.partitions | 50 | 5 | false | true | false |
| transaction.state.log.replication.factor | 3 | 4 | false | true | false |
| transaction.state.log.segment.bytes | 104857600 | 5 | false | true | false |
| transaction.two.phase.commit.enable | false | 5 | false | true | false |
| transactional.id.expiration.ms | 604800000 | 5 | false | true | false |
| unclean.leader.election.enable | false | 5 | false | false | false |

### Broker `2`

| name | value | source | default | readonly | sensitive |
| --- | --- | --- | --- | --- | --- |
| add.partitions.to.txn.retry.backoff.max.ms | 100 | 5 | false | true | false |
| add.partitions.to.txn.retry.backoff.ms | 20 | 5 | false | true | false |
| advertised.listeners | DOCKER://kafka-2:9092,HOST://localhost:9095 | 4 | false | true | false |
| allow.plaintext.listener |  | 4 | false | true | true |
| alter.config.policy.class.name |  | 5 | false | true | false |
| alter.log.dirs.replication.quota.window.num | 11 | 5 | false | true | false |
| alter.log.dirs.replication.quota.window.size.seconds | 1 | 5 | false | true | false |
| authorizer.class.name |  | 5 | false | true | false |
| auto.create.topics.enable | false | 4 | false | true | false |
| auto.leader.rebalance.enable | true | 5 | false | true | false |
| background.threads | 10 | 5 | false | false | false |
| broker.heartbeat.interval.ms | 2000 | 5 | false | true | false |
| broker.id | 2 | 4 | false | true | false |
| broker.rack |  | 5 | false | true | false |
| broker.session.timeout.ms | 9000 | 5 | false | true | false |
| client.quota.callback.class |  | 5 | false | true | false |
| cluster.id |  | 4 | false | true | true |
| compression.gzip.level | -1 | 5 | false | false | false |
| compression.lz4.level | 9 | 5 | false | false | false |
| compression.type | producer | 5 | false | false | false |
| compression.zstd.level | 3 | 5 | false | false | false |
| config.providers |  | 5 | false | false | false |
| connection.failed.authentication.delay.ms | 100 | 5 | false | true | false |
| connections.max.idle.ms | 600000 | 5 | false | true | false |
| connections.max.reauth.ms | 0 | 5 | false | true | false |
| controlled.shutdown.enable | true | 5 | false | true | false |
| controller.listener.names | CONTROLLER | 4 | false | true | false |
| controller.quorum.append.linger.ms | 25 | 5 | false | true | false |
| controller.quorum.auto.join.enable | false | 5 | false | true | false |
| controller.quorum.bootstrap.servers |  | 5 | false | true | false |
| controller.quorum.election.backoff.max.ms | 1000 | 5 | false | true | false |
| controller.quorum.election.timeout.ms | 1000 | 5 | false | true | false |
| controller.quorum.fetch.timeout.ms | 2000 | 5 | false | true | false |
| controller.quorum.request.timeout.ms | 2000 | 5 | false | true | false |
| controller.quorum.retry.backoff.ms | 20 | 5 | false | true | false |
| controller.quorum.voters | 1@kafka-1:9093,2@kafka-2:9093,3@kafka-3:9093 | 4 | false | true | false |
| controller.quota.window.num | 11 | 5 | false | true | false |
| controller.quota.window.size.seconds | 1 | 5 | false | true | false |
| controller.socket.timeout.ms | 30000 | 5 | false | true | false |
| create.topic.policy.class.name |  | 5 | false | true | false |
| default.replication.factor | 3 | 4 | false | true | false |
| delegation.token.expiry.check.interval.ms | 3600000 | 5 | false | true | false |
| delegation.token.expiry.time.ms | 86400000 | 5 | false | true | false |
| delegation.token.max.lifetime.ms | 604800000 | 5 | false | true | false |
| delegation.token.secret.key |  | 5 | false | true | true |
| delete.records.purgatory.purge.interval.requests | 1 | 5 | false | true | false |
| delete.topic.enable | true | 5 | false | true | false |
| early.start.listeners |  | 5 | false | true | false |
| fetch.max.bytes | 57671680 | 5 | false | true | false |
| fetch.purgatory.purge.interval.requests | 1000 | 5 | false | true | false |
| group.consumer.assignors | uniform,range | 5 | false | true | false |
| group.consumer.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.consumer.max.heartbeat.interval.ms | 15000 | 5 | false | true | false |
| group.consumer.max.session.timeout.ms | 60000 | 5 | false | true | false |
| group.consumer.max.size | 2147483647 | 5 | false | true | false |
| group.consumer.migration.policy | bidirectional | 5 | false | true | false |
| group.consumer.min.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.consumer.min.session.timeout.ms | 45000 | 5 | false | true | false |
| group.consumer.session.timeout.ms | 45000 | 5 | false | true | false |
| group.coordinator.append.linger.ms | -1 | 5 | false | true | false |
| group.coordinator.rebalance.protocols | classic,consumer,streams | 5 | false | true | false |
| group.coordinator.threads | 4 | 5 | false | true | false |
| group.initial.rebalance.delay.ms | 3000 | 5 | false | true | false |
| group.max.session.timeout.ms | 1800000 | 5 | false | true | false |
| group.max.size | 2147483647 | 5 | false | true | false |
| group.min.session.timeout.ms | 6000 | 5 | false | true | false |
| group.share.assignors | simple | 5 | false | true | false |
| group.share.delivery.count.limit | 5 | 5 | false | true | false |
| group.share.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.share.max.heartbeat.interval.ms | 15000 | 5 | false | true | false |
| group.share.max.record.lock.duration.ms | 60000 | 5 | false | true | false |
| group.share.max.session.timeout.ms | 60000 | 5 | false | true | false |
| group.share.max.share.sessions | 2000 | 5 | false | true | false |
| group.share.max.size | 200 | 5 | false | true | false |
| group.share.min.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.share.min.record.lock.duration.ms | 15000 | 5 | false | true | false |
| group.share.min.session.timeout.ms | 45000 | 5 | false | true | false |
| group.share.partition.max.record.locks | 2000 | 5 | false | true | false |
| group.share.record.lock.duration.ms | 30000 | 5 | false | true | false |
| group.share.session.timeout.ms | 45000 | 5 | false | true | false |
| group.streams.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.streams.initial.rebalance.delay.ms | 3000 | 5 | false | true | false |
| group.streams.max.heartbeat.interval.ms | 15000 | 5 | false | true | false |
| group.streams.max.session.timeout.ms | 60000 | 5 | false | true | false |
| group.streams.max.size | 2147483647 | 5 | false | true | false |
| group.streams.max.standby.replicas | 2 | 5 | false | true | false |
| group.streams.min.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.streams.min.session.timeout.ms | 45000 | 5 | false | true | false |
| group.streams.num.standby.replicas | 0 | 5 | false | true | false |
| group.streams.session.timeout.ms | 45000 | 5 | false | true | false |
| initial.broker.registration.timeout.ms | 60000 | 5 | false | true | false |
| inter.broker.listener.name | DOCKER | 4 | false | true | false |
| kafka.metrics.polling.interval.secs | 10 | 5 | false | true | false |
| kafka.metrics.reporters |  | 5 | false | true | false |
| leader.imbalance.check.interval.seconds | 300 | 5 | false | true | false |
| listener.security.protocol.map | CONTROLLER:PLAINTEXT,DOCKER:PLAINTEXT,HOST:PLAINTEXT | 4 | false | false | false |
| listeners | DOCKER://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093,HOST://0.0.0.0:9094 | 4 | false | false | false |
| log.cleaner.backoff.ms | 15000 | 5 | false | false | false |
| log.cleaner.dedupe.buffer.size | 134217728 | 5 | false | false | false |
| log.cleaner.delete.retention.ms | 86400000 | 5 | false | false | false |
| log.cleaner.enable | true | 5 | false | true | false |
| log.cleaner.io.buffer.load.factor | 0.9 | 5 | false | false | false |
| log.cleaner.io.buffer.size | 524288 | 5 | false | false | false |
| log.cleaner.io.max.bytes.per.second | 1.7976931348623157E308 | 5 | false | false | false |
| log.cleaner.max.compaction.lag.ms | 9223372036854775807 | 5 | false | false | false |
| log.cleaner.min.cleanable.ratio | 0.5 | 5 | false | false | false |
| log.cleaner.min.compaction.lag.ms | 0 | 5 | false | false | false |
| log.cleaner.threads | 1 | 5 | false | false | false |
| log.cleanup.policy | delete | 5 | false | false | false |
| log.dir | /tmp/kafka-logs | 5 | false | true | false |
| log.dir.failure.timeout.ms | 30000 | 5 | false | true | false |
| log.dirs |  | 5 | false | true | false |
| log.flush.interval.messages | 9223372036854775807 | 5 | false | false | false |
| log.flush.interval.ms |  | 5 | false | false | false |
| log.flush.offset.checkpoint.interval.ms | 60000 | 5 | false | true | false |
| log.flush.scheduler.interval.ms | 9223372036854775807 | 5 | false | true | false |
| log.flush.start.offset.checkpoint.interval.ms | 60000 | 5 | false | true | false |
| log.index.interval.bytes | 4096 | 5 | false | false | false |
| log.index.size.max.bytes | 10485760 | 5 | false | false | false |
| log.local.retention.bytes | -2 | 5 | false | false | false |
| log.local.retention.ms | -2 | 5 | false | false | false |
| log.message.timestamp.after.max.ms | 3600000 | 5 | false | false | false |
| log.message.timestamp.before.max.ms | 9223372036854775807 | 5 | false | false | false |
| log.message.timestamp.type | CreateTime | 5 | false | false | false |
| log.preallocate | false | 5 | false | false | false |
| log.retention.bytes | -1 | 5 | false | false | false |
| log.retention.check.interval.ms | 300000 | 5 | false | true | false |
| log.retention.hours | 168 | 5 | false | true | false |
| log.retention.minutes |  | 5 | false | true | false |
| log.retention.ms |  | 5 | false | false | false |
| log.roll.hours | 168 | 5 | false | true | false |
| log.roll.jitter.hours | 0 | 5 | false | true | false |
| log.roll.jitter.ms |  | 5 | false | false | false |
| log.roll.ms |  | 5 | false | false | false |
| log.segment.bytes | 1073741824 | 5 | false | false | false |
| log.segment.delete.delay.ms | 60000 | 5 | false | false | false |
| max.connection.creation.rate | 2147483647 | 5 | false | false | false |
| max.connections | 2147483647 | 5 | false | false | false |
| max.connections.per.ip | 2147483647 | 5 | false | false | false |
| max.connections.per.ip.overrides |  | 5 | false | false | false |
| max.incremental.fetch.session.cache.slots | 1000 | 5 | false | true | false |
| max.request.partition.size.limit | 2000 | 5 | false | true | false |
| message.max.bytes | 1048588 | 5 | false | false | false |
| metadata.log.dir |  | 5 | false | true | false |
| metadata.log.max.record.bytes.between.snapshots | 20971520 | 5 | false | true | false |
| metadata.log.max.snapshot.interval.ms | 3600000 | 5 | false | true | false |
| metadata.log.segment.bytes | 1073741824 | 5 | false | true | false |
| metadata.log.segment.ms | 604800000 | 5 | false | true | false |
| metadata.max.idle.interval.ms | 500 | 5 | false | true | false |
| metadata.max.retention.bytes | 104857600 | 5 | false | true | false |
| metadata.max.retention.ms | 604800000 | 5 | false | true | false |
| metric.reporters | org.apache.kafka.common.metrics.JmxReporter | 5 | false | false | false |
| metrics.num.samples | 2 | 5 | false | true | false |
| metrics.recording.level | INFO | 5 | false | true | false |
| metrics.sample.window.ms | 30000 | 5 | false | true | false |
| min.insync.replicas | 2 | 3 | false | false | false |
| node.id | 2 | 4 | false | true | false |
| num.io.threads | 8 | 5 | false | false | false |
| num.network.threads | 3 | 5 | false | false | false |
| num.partitions | 1 | 5 | false | true | false |
| num.recovery.threads.per.data.dir | 2 | 5 | false | false | false |
| num.replica.alter.log.dirs.threads |  | 5 | false | true | false |
| num.replica.fetchers | 1 | 5 | false | false | false |
| offset.metadata.max.bytes | 4096 | 5 | false | true | false |
| offsets.commit.timeout.ms | 5000 | 5 | false | true | false |
| offsets.load.buffer.size | 5242880 | 5 | false | true | false |
| offsets.retention.check.interval.ms | 600000 | 5 | false | true | false |
| offsets.retention.minutes | 10080 | 5 | false | true | false |
| offsets.topic.compression.codec | 0 | 5 | false | true | false |
| offsets.topic.num.partitions | 50 | 5 | false | true | false |
| offsets.topic.replication.factor | 3 | 4 | false | true | false |
| offsets.topic.segment.bytes | 104857600 | 5 | false | true | false |
| principal.builder.class | org.apache.kafka.common.security.authenticator.DefaultKafkaPrincipalBuilder | 5 | false | false | false |
| process.roles | broker,controller | 4 | false | true | false |
| producer.id.expiration.ms | 86400000 | 5 | false | false | false |
| producer.purgatory.purge.interval.requests | 1000 | 5 | false | true | false |
| queued.max.request.bytes | -1 | 5 | false | true | false |
| queued.max.requests | 500 | 5 | false | true | false |
| quota.window.num | 11 | 5 | false | true | false |
| quota.window.size.seconds | 1 | 5 | false | true | false |
| remote.fetch.max.wait.ms | 500 | 5 | false | false | false |
| remote.list.offsets.request.timeout.ms | 30000 | 5 | false | false | false |
| remote.log.index.file.cache.total.size.bytes | 1073741824 | 5 | false | false | false |
| remote.log.manager.copier.thread.pool.size | 10 | 5 | false | false | false |
| remote.log.manager.copy.max.bytes.per.second | 9223372036854775807 | 5 | false | false | false |
| remote.log.manager.copy.quota.window.num | 11 | 5 | false | true | false |
| remote.log.manager.copy.quota.window.size.seconds | 1 | 5 | false | true | false |
| remote.log.manager.expiration.thread.pool.size | 10 | 5 | false | false | false |
| remote.log.manager.fetch.max.bytes.per.second | 9223372036854775807 | 5 | false | false | false |
| remote.log.manager.fetch.quota.window.num | 11 | 5 | false | true | false |
| remote.log.manager.fetch.quota.window.size.seconds | 1 | 5 | false | true | false |
| remote.log.manager.follower.thread.pool.size | 2 | 5 | false | false | false |
| remote.log.manager.task.interval.ms | 30000 | 5 | false | true | false |
| remote.log.manager.thread.pool.size | 2 | 5 | false | true | false |
| remote.log.metadata.custom.metadata.max.bytes | 128 | 5 | false | true | false |
| remote.log.metadata.manager.class.name | org.apache.kafka.server.log.remote.metadata.storage.TopicBasedRemoteLogMetadataManager | 5 | false | true | false |
| remote.log.metadata.manager.class.path |  | 5 | false | true | false |
| remote.log.metadata.manager.impl.prefix | rlmm.config. | 5 | false | true | false |
| remote.log.metadata.manager.listener.name |  | 5 | false | true | false |
| remote.log.reader.max.pending.tasks | 100 | 5 | false | true | false |
| remote.log.reader.threads | 10 | 5 | false | false | false |
| remote.log.storage.manager.class.name |  | 5 | false | true | false |
| remote.log.storage.manager.class.path |  | 5 | false | true | false |
| remote.log.storage.manager.impl.prefix | rsm.config. | 5 | false | true | false |
| remote.log.storage.system.enable | false | 5 | false | true | false |
| replica.fetch.backoff.ms | 1000 | 5 | false | true | false |
| replica.fetch.max.bytes | 1048576 | 5 | false | true | false |
| replica.fetch.min.bytes | 1 | 5 | false | true | false |
| replica.fetch.response.max.bytes | 10485760 | 5 | false | true | false |
| replica.fetch.wait.max.ms | 500 | 5 | false | true | false |
| replica.high.watermark.checkpoint.interval.ms | 5000 | 5 | false | true | false |
| replica.lag.time.max.ms | 30000 | 5 | false | true | false |
| replica.selector.class |  | 5 | false | true | false |
| replica.socket.receive.buffer.bytes | 65536 | 5 | false | true | false |
| replica.socket.timeout.ms | 30000 | 5 | false | true | false |
| replication.quota.window.num | 11 | 5 | false | true | false |
| replication.quota.window.size.seconds | 1 | 5 | false | true | false |
| request.timeout.ms | 30000 | 5 | false | true | false |
| sasl.client.callback.handler.class |  | 5 | false | true | false |
| sasl.enabled.mechanisms | GSSAPI | 5 | false | false | false |
| sasl.jaas.config |  | 5 | false | false | true |
| sasl.kerberos.kinit.cmd | /usr/bin/kinit | 5 | false | false | false |
| sasl.kerberos.min.time.before.relogin | 60000 | 5 | false | false | false |
| sasl.kerberos.principal.to.local.rules | DEFAULT | 5 | false | false | false |
| sasl.kerberos.service.name |  | 5 | false | false | false |
| sasl.kerberos.ticket.renew.jitter | 0.05 | 5 | false | false | false |
| sasl.kerberos.ticket.renew.window.factor | 0.8 | 5 | false | false | false |
| sasl.login.callback.handler.class |  | 5 | false | true | false |
| sasl.login.class |  | 5 | false | true | false |
| sasl.login.connect.timeout.ms |  | 5 | false | true | false |
| sasl.login.read.timeout.ms |  | 5 | false | true | false |
| sasl.login.refresh.buffer.seconds | 300 | 5 | false | false | false |
| sasl.login.refresh.min.period.seconds | 60 | 5 | false | false | false |
| sasl.login.refresh.window.factor | 0.8 | 5 | false | false | false |
| sasl.login.refresh.window.jitter | 0.05 | 5 | false | false | false |
| sasl.login.retry.backoff.max.ms | 10000 | 5 | false | true | false |
| sasl.login.retry.backoff.ms | 100 | 5 | false | true | false |
| sasl.mechanism.controller.protocol | GSSAPI | 5 | false | true | false |
| sasl.mechanism.inter.broker.protocol | GSSAPI | 5 | false | false | false |
| sasl.oauthbearer.assertion.algorithm | RS256 | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.aud |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.exp.seconds | 300 | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.iss |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.jti.include | false | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.nbf.seconds | 60 | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.sub |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.file |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.private.key.file |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.private.key.passphrase |  | 5 | false | true | true |
| sasl.oauthbearer.assertion.template.file |  | 5 | false | true | false |
| sasl.oauthbearer.client.credentials.client.id |  | 5 | false | true | false |
| sasl.oauthbearer.client.credentials.client.secret |  | 5 | false | true | true |
| sasl.oauthbearer.clock.skew.seconds | 30 | 5 | false | true | false |
| sasl.oauthbearer.expected.audience |  | 5 | false | true | false |
| sasl.oauthbearer.expected.issuer |  | 5 | false | true | false |
| sasl.oauthbearer.jwks.endpoint.refresh.ms | 3600000 | 5 | false | true | false |
| sasl.oauthbearer.jwks.endpoint.retry.backoff.max.ms | 10000 | 5 | false | true | false |
| sasl.oauthbearer.jwks.endpoint.retry.backoff.ms | 100 | 5 | false | true | false |
| sasl.oauthbearer.jwks.endpoint.url |  | 5 | false | true | false |
| sasl.oauthbearer.jwt.retriever.class | org.apache.kafka.common.security.oauthbearer.DefaultJwtRetriever | 5 | false | true | false |
| sasl.oauthbearer.jwt.validator.class | org.apache.kafka.common.security.oauthbearer.DefaultJwtValidator | 5 | false | true | false |
| sasl.oauthbearer.scope |  | 5 | false | true | false |
| sasl.oauthbearer.scope.claim.name | scope | 5 | false | true | false |
| sasl.oauthbearer.sub.claim.name | sub | 5 | false | true | false |
| sasl.oauthbearer.token.endpoint.url |  | 5 | false | true | false |
| sasl.server.callback.handler.class |  | 5 | false | true | false |
| sasl.server.max.receive.size | 524288 | 5 | false | true | false |
| security.inter.broker.protocol | PLAINTEXT | 5 | false | true | false |
| security.providers |  | 5 | false | true | false |
| share.coordinator.append.linger.ms | -1 | 5 | false | true | false |
| share.coordinator.load.buffer.size | 5242880 | 5 | false | true | false |
| share.coordinator.snapshot.update.records.per.snapshot | 500 | 5 | false | true | false |
| share.coordinator.state.topic.compression.codec | 0 | 5 | false | true | false |
| share.coordinator.state.topic.min.isr | 2 | 5 | false | true | false |
| share.coordinator.state.topic.num.partitions | 50 | 5 | false | true | false |
| share.coordinator.state.topic.replication.factor | 3 | 5 | false | true | false |
| share.coordinator.state.topic.segment.bytes | 104857600 | 5 | false | true | false |
| share.coordinator.threads | 1 | 5 | false | true | false |
| share.coordinator.write.timeout.ms | 5000 | 5 | false | true | false |
| share.fetch.purgatory.purge.interval.requests | 1000 | 5 | false | true | false |
| socket.connection.setup.timeout.max.ms | 30000 | 5 | false | true | false |
| socket.connection.setup.timeout.ms | 10000 | 5 | false | true | false |
| socket.listen.backlog.size | 50 | 5 | false | true | false |
| socket.receive.buffer.bytes | 102400 | 5 | false | true | false |
| socket.request.max.bytes | 104857600 | 5 | false | true | false |
| socket.send.buffer.bytes | 102400 | 5 | false | true | false |
| ssl.allow.dn.changes | false | 5 | false | true | false |
| ssl.allow.san.changes | false | 5 | false | true | false |
| ssl.cipher.suites |  | 5 | false | false | false |
| ssl.client.auth | none | 5 | false | false | false |
| ssl.enabled.protocols | TLSv1.2,TLSv1.3 | 5 | false | false | false |
| ssl.endpoint.identification.algorithm | https | 5 | false | false | false |
| ssl.engine.factory.class |  | 5 | false | false | false |
| ssl.key.password |  | 5 | false | false | true |
| ssl.keymanager.algorithm | SunX509 | 5 | false | false | false |
| ssl.keystore.certificate.chain |  | 5 | false | false | true |
| ssl.keystore.key |  | 5 | false | false | true |
| ssl.keystore.location |  | 5 | false | false | false |
| ssl.keystore.password |  | 5 | false | false | true |
| ssl.keystore.type | JKS | 5 | false | false | false |
| ssl.principal.mapping.rules | DEFAULT | 5 | false | true | false |
| ssl.protocol | TLSv1.3 | 5 | false | false | false |
| ssl.provider |  | 5 | false | false | false |
| ssl.secure.random.implementation |  | 5 | false | false | false |
| ssl.trustmanager.algorithm | PKIX | 5 | false | false | false |
| ssl.truststore.certificates |  | 5 | false | false | true |
| ssl.truststore.location |  | 5 | false | false | false |
| ssl.truststore.password |  | 5 | false | false | true |
| ssl.truststore.type | JKS | 5 | false | false | false |
| telemetry.max.bytes | 1048576 | 5 | false | true | false |
| transaction.abort.timed.out.transaction.cleanup.interval.ms | 10000 | 5 | false | true | false |
| transaction.max.timeout.ms | 900000 | 5 | false | true | false |
| transaction.partition.verification.enable | true | 5 | false | false | false |
| transaction.remove.expired.transaction.cleanup.interval.ms | 3600000 | 5 | false | true | false |
| transaction.state.log.load.buffer.size | 5242880 | 5 | false | true | false |
| transaction.state.log.min.isr | 2 | 4 | false | true | false |
| transaction.state.log.num.partitions | 50 | 5 | false | true | false |
| transaction.state.log.replication.factor | 3 | 4 | false | true | false |
| transaction.state.log.segment.bytes | 104857600 | 5 | false | true | false |
| transaction.two.phase.commit.enable | false | 5 | false | true | false |
| transactional.id.expiration.ms | 604800000 | 5 | false | true | false |
| unclean.leader.election.enable | false | 5 | false | false | false |

### Broker `3`

| name | value | source | default | readonly | sensitive |
| --- | --- | --- | --- | --- | --- |
| add.partitions.to.txn.retry.backoff.max.ms | 100 | 5 | false | true | false |
| add.partitions.to.txn.retry.backoff.ms | 20 | 5 | false | true | false |
| advertised.listeners | DOCKER://kafka-3:9092,HOST://localhost:9096 | 4 | false | true | false |
| allow.plaintext.listener |  | 4 | false | true | true |
| alter.config.policy.class.name |  | 5 | false | true | false |
| alter.log.dirs.replication.quota.window.num | 11 | 5 | false | true | false |
| alter.log.dirs.replication.quota.window.size.seconds | 1 | 5 | false | true | false |
| authorizer.class.name |  | 5 | false | true | false |
| auto.create.topics.enable | false | 4 | false | true | false |
| auto.leader.rebalance.enable | true | 5 | false | true | false |
| background.threads | 10 | 5 | false | false | false |
| broker.heartbeat.interval.ms | 2000 | 5 | false | true | false |
| broker.id | 3 | 4 | false | true | false |
| broker.rack |  | 5 | false | true | false |
| broker.session.timeout.ms | 9000 | 5 | false | true | false |
| client.quota.callback.class |  | 5 | false | true | false |
| cluster.id |  | 4 | false | true | true |
| compression.gzip.level | -1 | 5 | false | false | false |
| compression.lz4.level | 9 | 5 | false | false | false |
| compression.type | producer | 5 | false | false | false |
| compression.zstd.level | 3 | 5 | false | false | false |
| config.providers |  | 5 | false | false | false |
| connection.failed.authentication.delay.ms | 100 | 5 | false | true | false |
| connections.max.idle.ms | 600000 | 5 | false | true | false |
| connections.max.reauth.ms | 0 | 5 | false | true | false |
| controlled.shutdown.enable | true | 5 | false | true | false |
| controller.listener.names | CONTROLLER | 4 | false | true | false |
| controller.quorum.append.linger.ms | 25 | 5 | false | true | false |
| controller.quorum.auto.join.enable | false | 5 | false | true | false |
| controller.quorum.bootstrap.servers |  | 5 | false | true | false |
| controller.quorum.election.backoff.max.ms | 1000 | 5 | false | true | false |
| controller.quorum.election.timeout.ms | 1000 | 5 | false | true | false |
| controller.quorum.fetch.timeout.ms | 2000 | 5 | false | true | false |
| controller.quorum.request.timeout.ms | 2000 | 5 | false | true | false |
| controller.quorum.retry.backoff.ms | 20 | 5 | false | true | false |
| controller.quorum.voters | 1@kafka-1:9093,2@kafka-2:9093,3@kafka-3:9093 | 4 | false | true | false |
| controller.quota.window.num | 11 | 5 | false | true | false |
| controller.quota.window.size.seconds | 1 | 5 | false | true | false |
| controller.socket.timeout.ms | 30000 | 5 | false | true | false |
| create.topic.policy.class.name |  | 5 | false | true | false |
| default.replication.factor | 3 | 4 | false | true | false |
| delegation.token.expiry.check.interval.ms | 3600000 | 5 | false | true | false |
| delegation.token.expiry.time.ms | 86400000 | 5 | false | true | false |
| delegation.token.max.lifetime.ms | 604800000 | 5 | false | true | false |
| delegation.token.secret.key |  | 5 | false | true | true |
| delete.records.purgatory.purge.interval.requests | 1 | 5 | false | true | false |
| delete.topic.enable | true | 5 | false | true | false |
| early.start.listeners |  | 5 | false | true | false |
| fetch.max.bytes | 57671680 | 5 | false | true | false |
| fetch.purgatory.purge.interval.requests | 1000 | 5 | false | true | false |
| group.consumer.assignors | uniform,range | 5 | false | true | false |
| group.consumer.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.consumer.max.heartbeat.interval.ms | 15000 | 5 | false | true | false |
| group.consumer.max.session.timeout.ms | 60000 | 5 | false | true | false |
| group.consumer.max.size | 2147483647 | 5 | false | true | false |
| group.consumer.migration.policy | bidirectional | 5 | false | true | false |
| group.consumer.min.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.consumer.min.session.timeout.ms | 45000 | 5 | false | true | false |
| group.consumer.session.timeout.ms | 45000 | 5 | false | true | false |
| group.coordinator.append.linger.ms | -1 | 5 | false | true | false |
| group.coordinator.rebalance.protocols | classic,consumer,streams | 5 | false | true | false |
| group.coordinator.threads | 4 | 5 | false | true | false |
| group.initial.rebalance.delay.ms | 3000 | 5 | false | true | false |
| group.max.session.timeout.ms | 1800000 | 5 | false | true | false |
| group.max.size | 2147483647 | 5 | false | true | false |
| group.min.session.timeout.ms | 6000 | 5 | false | true | false |
| group.share.assignors | simple | 5 | false | true | false |
| group.share.delivery.count.limit | 5 | 5 | false | true | false |
| group.share.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.share.max.heartbeat.interval.ms | 15000 | 5 | false | true | false |
| group.share.max.record.lock.duration.ms | 60000 | 5 | false | true | false |
| group.share.max.session.timeout.ms | 60000 | 5 | false | true | false |
| group.share.max.share.sessions | 2000 | 5 | false | true | false |
| group.share.max.size | 200 | 5 | false | true | false |
| group.share.min.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.share.min.record.lock.duration.ms | 15000 | 5 | false | true | false |
| group.share.min.session.timeout.ms | 45000 | 5 | false | true | false |
| group.share.partition.max.record.locks | 2000 | 5 | false | true | false |
| group.share.record.lock.duration.ms | 30000 | 5 | false | true | false |
| group.share.session.timeout.ms | 45000 | 5 | false | true | false |
| group.streams.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.streams.initial.rebalance.delay.ms | 3000 | 5 | false | true | false |
| group.streams.max.heartbeat.interval.ms | 15000 | 5 | false | true | false |
| group.streams.max.session.timeout.ms | 60000 | 5 | false | true | false |
| group.streams.max.size | 2147483647 | 5 | false | true | false |
| group.streams.max.standby.replicas | 2 | 5 | false | true | false |
| group.streams.min.heartbeat.interval.ms | 5000 | 5 | false | true | false |
| group.streams.min.session.timeout.ms | 45000 | 5 | false | true | false |
| group.streams.num.standby.replicas | 0 | 5 | false | true | false |
| group.streams.session.timeout.ms | 45000 | 5 | false | true | false |
| initial.broker.registration.timeout.ms | 60000 | 5 | false | true | false |
| inter.broker.listener.name | DOCKER | 4 | false | true | false |
| kafka.metrics.polling.interval.secs | 10 | 5 | false | true | false |
| kafka.metrics.reporters |  | 5 | false | true | false |
| leader.imbalance.check.interval.seconds | 300 | 5 | false | true | false |
| listener.security.protocol.map | CONTROLLER:PLAINTEXT,DOCKER:PLAINTEXT,HOST:PLAINTEXT | 4 | false | false | false |
| listeners | DOCKER://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093,HOST://0.0.0.0:9094 | 4 | false | false | false |
| log.cleaner.backoff.ms | 15000 | 5 | false | false | false |
| log.cleaner.dedupe.buffer.size | 134217728 | 5 | false | false | false |
| log.cleaner.delete.retention.ms | 86400000 | 5 | false | false | false |
| log.cleaner.enable | true | 5 | false | true | false |
| log.cleaner.io.buffer.load.factor | 0.9 | 5 | false | false | false |
| log.cleaner.io.buffer.size | 524288 | 5 | false | false | false |
| log.cleaner.io.max.bytes.per.second | 1.7976931348623157E308 | 5 | false | false | false |
| log.cleaner.max.compaction.lag.ms | 9223372036854775807 | 5 | false | false | false |
| log.cleaner.min.cleanable.ratio | 0.5 | 5 | false | false | false |
| log.cleaner.min.compaction.lag.ms | 0 | 5 | false | false | false |
| log.cleaner.threads | 1 | 5 | false | false | false |
| log.cleanup.policy | delete | 5 | false | false | false |
| log.dir | /tmp/kafka-logs | 5 | false | true | false |
| log.dir.failure.timeout.ms | 30000 | 5 | false | true | false |
| log.dirs |  | 5 | false | true | false |
| log.flush.interval.messages | 9223372036854775807 | 5 | false | false | false |
| log.flush.interval.ms |  | 5 | false | false | false |
| log.flush.offset.checkpoint.interval.ms | 60000 | 5 | false | true | false |
| log.flush.scheduler.interval.ms | 9223372036854775807 | 5 | false | true | false |
| log.flush.start.offset.checkpoint.interval.ms | 60000 | 5 | false | true | false |
| log.index.interval.bytes | 4096 | 5 | false | false | false |
| log.index.size.max.bytes | 10485760 | 5 | false | false | false |
| log.local.retention.bytes | -2 | 5 | false | false | false |
| log.local.retention.ms | -2 | 5 | false | false | false |
| log.message.timestamp.after.max.ms | 3600000 | 5 | false | false | false |
| log.message.timestamp.before.max.ms | 9223372036854775807 | 5 | false | false | false |
| log.message.timestamp.type | CreateTime | 5 | false | false | false |
| log.preallocate | false | 5 | false | false | false |
| log.retention.bytes | -1 | 5 | false | false | false |
| log.retention.check.interval.ms | 300000 | 5 | false | true | false |
| log.retention.hours | 168 | 5 | false | true | false |
| log.retention.minutes |  | 5 | false | true | false |
| log.retention.ms |  | 5 | false | false | false |
| log.roll.hours | 168 | 5 | false | true | false |
| log.roll.jitter.hours | 0 | 5 | false | true | false |
| log.roll.jitter.ms |  | 5 | false | false | false |
| log.roll.ms |  | 5 | false | false | false |
| log.segment.bytes | 1073741824 | 5 | false | false | false |
| log.segment.delete.delay.ms | 60000 | 5 | false | false | false |
| max.connection.creation.rate | 2147483647 | 5 | false | false | false |
| max.connections | 2147483647 | 5 | false | false | false |
| max.connections.per.ip | 2147483647 | 5 | false | false | false |
| max.connections.per.ip.overrides |  | 5 | false | false | false |
| max.incremental.fetch.session.cache.slots | 1000 | 5 | false | true | false |
| max.request.partition.size.limit | 2000 | 5 | false | true | false |
| message.max.bytes | 1048588 | 5 | false | false | false |
| metadata.log.dir |  | 5 | false | true | false |
| metadata.log.max.record.bytes.between.snapshots | 20971520 | 5 | false | true | false |
| metadata.log.max.snapshot.interval.ms | 3600000 | 5 | false | true | false |
| metadata.log.segment.bytes | 1073741824 | 5 | false | true | false |
| metadata.log.segment.ms | 604800000 | 5 | false | true | false |
| metadata.max.idle.interval.ms | 500 | 5 | false | true | false |
| metadata.max.retention.bytes | 104857600 | 5 | false | true | false |
| metadata.max.retention.ms | 604800000 | 5 | false | true | false |
| metric.reporters | org.apache.kafka.common.metrics.JmxReporter | 5 | false | false | false |
| metrics.num.samples | 2 | 5 | false | true | false |
| metrics.recording.level | INFO | 5 | false | true | false |
| metrics.sample.window.ms | 30000 | 5 | false | true | false |
| min.insync.replicas | 2 | 3 | false | false | false |
| node.id | 3 | 4 | false | true | false |
| num.io.threads | 8 | 5 | false | false | false |
| num.network.threads | 3 | 5 | false | false | false |
| num.partitions | 1 | 5 | false | true | false |
| num.recovery.threads.per.data.dir | 2 | 5 | false | false | false |
| num.replica.alter.log.dirs.threads |  | 5 | false | true | false |
| num.replica.fetchers | 1 | 5 | false | false | false |
| offset.metadata.max.bytes | 4096 | 5 | false | true | false |
| offsets.commit.timeout.ms | 5000 | 5 | false | true | false |
| offsets.load.buffer.size | 5242880 | 5 | false | true | false |
| offsets.retention.check.interval.ms | 600000 | 5 | false | true | false |
| offsets.retention.minutes | 10080 | 5 | false | true | false |
| offsets.topic.compression.codec | 0 | 5 | false | true | false |
| offsets.topic.num.partitions | 50 | 5 | false | true | false |
| offsets.topic.replication.factor | 3 | 4 | false | true | false |
| offsets.topic.segment.bytes | 104857600 | 5 | false | true | false |
| principal.builder.class | org.apache.kafka.common.security.authenticator.DefaultKafkaPrincipalBuilder | 5 | false | false | false |
| process.roles | broker,controller | 4 | false | true | false |
| producer.id.expiration.ms | 86400000 | 5 | false | false | false |
| producer.purgatory.purge.interval.requests | 1000 | 5 | false | true | false |
| queued.max.request.bytes | -1 | 5 | false | true | false |
| queued.max.requests | 500 | 5 | false | true | false |
| quota.window.num | 11 | 5 | false | true | false |
| quota.window.size.seconds | 1 | 5 | false | true | false |
| remote.fetch.max.wait.ms | 500 | 5 | false | false | false |
| remote.list.offsets.request.timeout.ms | 30000 | 5 | false | false | false |
| remote.log.index.file.cache.total.size.bytes | 1073741824 | 5 | false | false | false |
| remote.log.manager.copier.thread.pool.size | 10 | 5 | false | false | false |
| remote.log.manager.copy.max.bytes.per.second | 9223372036854775807 | 5 | false | false | false |
| remote.log.manager.copy.quota.window.num | 11 | 5 | false | true | false |
| remote.log.manager.copy.quota.window.size.seconds | 1 | 5 | false | true | false |
| remote.log.manager.expiration.thread.pool.size | 10 | 5 | false | false | false |
| remote.log.manager.fetch.max.bytes.per.second | 9223372036854775807 | 5 | false | false | false |
| remote.log.manager.fetch.quota.window.num | 11 | 5 | false | true | false |
| remote.log.manager.fetch.quota.window.size.seconds | 1 | 5 | false | true | false |
| remote.log.manager.follower.thread.pool.size | 2 | 5 | false | false | false |
| remote.log.manager.task.interval.ms | 30000 | 5 | false | true | false |
| remote.log.manager.thread.pool.size | 2 | 5 | false | true | false |
| remote.log.metadata.custom.metadata.max.bytes | 128 | 5 | false | true | false |
| remote.log.metadata.manager.class.name | org.apache.kafka.server.log.remote.metadata.storage.TopicBasedRemoteLogMetadataManager | 5 | false | true | false |
| remote.log.metadata.manager.class.path |  | 5 | false | true | false |
| remote.log.metadata.manager.impl.prefix | rlmm.config. | 5 | false | true | false |
| remote.log.metadata.manager.listener.name |  | 5 | false | true | false |
| remote.log.reader.max.pending.tasks | 100 | 5 | false | true | false |
| remote.log.reader.threads | 10 | 5 | false | false | false |
| remote.log.storage.manager.class.name |  | 5 | false | true | false |
| remote.log.storage.manager.class.path |  | 5 | false | true | false |
| remote.log.storage.manager.impl.prefix | rsm.config. | 5 | false | true | false |
| remote.log.storage.system.enable | false | 5 | false | true | false |
| replica.fetch.backoff.ms | 1000 | 5 | false | true | false |
| replica.fetch.max.bytes | 1048576 | 5 | false | true | false |
| replica.fetch.min.bytes | 1 | 5 | false | true | false |
| replica.fetch.response.max.bytes | 10485760 | 5 | false | true | false |
| replica.fetch.wait.max.ms | 500 | 5 | false | true | false |
| replica.high.watermark.checkpoint.interval.ms | 5000 | 5 | false | true | false |
| replica.lag.time.max.ms | 30000 | 5 | false | true | false |
| replica.selector.class |  | 5 | false | true | false |
| replica.socket.receive.buffer.bytes | 65536 | 5 | false | true | false |
| replica.socket.timeout.ms | 30000 | 5 | false | true | false |
| replication.quota.window.num | 11 | 5 | false | true | false |
| replication.quota.window.size.seconds | 1 | 5 | false | true | false |
| request.timeout.ms | 30000 | 5 | false | true | false |
| sasl.client.callback.handler.class |  | 5 | false | true | false |
| sasl.enabled.mechanisms | GSSAPI | 5 | false | false | false |
| sasl.jaas.config |  | 5 | false | false | true |
| sasl.kerberos.kinit.cmd | /usr/bin/kinit | 5 | false | false | false |
| sasl.kerberos.min.time.before.relogin | 60000 | 5 | false | false | false |
| sasl.kerberos.principal.to.local.rules | DEFAULT | 5 | false | false | false |
| sasl.kerberos.service.name |  | 5 | false | false | false |
| sasl.kerberos.ticket.renew.jitter | 0.05 | 5 | false | false | false |
| sasl.kerberos.ticket.renew.window.factor | 0.8 | 5 | false | false | false |
| sasl.login.callback.handler.class |  | 5 | false | true | false |
| sasl.login.class |  | 5 | false | true | false |
| sasl.login.connect.timeout.ms |  | 5 | false | true | false |
| sasl.login.read.timeout.ms |  | 5 | false | true | false |
| sasl.login.refresh.buffer.seconds | 300 | 5 | false | false | false |
| sasl.login.refresh.min.period.seconds | 60 | 5 | false | false | false |
| sasl.login.refresh.window.factor | 0.8 | 5 | false | false | false |
| sasl.login.refresh.window.jitter | 0.05 | 5 | false | false | false |
| sasl.login.retry.backoff.max.ms | 10000 | 5 | false | true | false |
| sasl.login.retry.backoff.ms | 100 | 5 | false | true | false |
| sasl.mechanism.controller.protocol | GSSAPI | 5 | false | true | false |
| sasl.mechanism.inter.broker.protocol | GSSAPI | 5 | false | false | false |
| sasl.oauthbearer.assertion.algorithm | RS256 | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.aud |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.exp.seconds | 300 | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.iss |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.jti.include | false | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.nbf.seconds | 60 | 5 | false | true | false |
| sasl.oauthbearer.assertion.claim.sub |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.file |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.private.key.file |  | 5 | false | true | false |
| sasl.oauthbearer.assertion.private.key.passphrase |  | 5 | false | true | true |
| sasl.oauthbearer.assertion.template.file |  | 5 | false | true | false |
| sasl.oauthbearer.client.credentials.client.id |  | 5 | false | true | false |
| sasl.oauthbearer.client.credentials.client.secret |  | 5 | false | true | true |
| sasl.oauthbearer.clock.skew.seconds | 30 | 5 | false | true | false |
| sasl.oauthbearer.expected.audience |  | 5 | false | true | false |
| sasl.oauthbearer.expected.issuer |  | 5 | false | true | false |
| sasl.oauthbearer.jwks.endpoint.refresh.ms | 3600000 | 5 | false | true | false |
| sasl.oauthbearer.jwks.endpoint.retry.backoff.max.ms | 10000 | 5 | false | true | false |
| sasl.oauthbearer.jwks.endpoint.retry.backoff.ms | 100 | 5 | false | true | false |
| sasl.oauthbearer.jwks.endpoint.url |  | 5 | false | true | false |
| sasl.oauthbearer.jwt.retriever.class | org.apache.kafka.common.security.oauthbearer.DefaultJwtRetriever | 5 | false | true | false |
| sasl.oauthbearer.jwt.validator.class | org.apache.kafka.common.security.oauthbearer.DefaultJwtValidator | 5 | false | true | false |
| sasl.oauthbearer.scope |  | 5 | false | true | false |
| sasl.oauthbearer.scope.claim.name | scope | 5 | false | true | false |
| sasl.oauthbearer.sub.claim.name | sub | 5 | false | true | false |
| sasl.oauthbearer.token.endpoint.url |  | 5 | false | true | false |
| sasl.server.callback.handler.class |  | 5 | false | true | false |
| sasl.server.max.receive.size | 524288 | 5 | false | true | false |
| security.inter.broker.protocol | PLAINTEXT | 5 | false | true | false |
| security.providers |  | 5 | false | true | false |
| share.coordinator.append.linger.ms | -1 | 5 | false | true | false |
| share.coordinator.load.buffer.size | 5242880 | 5 | false | true | false |
| share.coordinator.snapshot.update.records.per.snapshot | 500 | 5 | false | true | false |
| share.coordinator.state.topic.compression.codec | 0 | 5 | false | true | false |
| share.coordinator.state.topic.min.isr | 2 | 5 | false | true | false |
| share.coordinator.state.topic.num.partitions | 50 | 5 | false | true | false |
| share.coordinator.state.topic.replication.factor | 3 | 5 | false | true | false |
| share.coordinator.state.topic.segment.bytes | 104857600 | 5 | false | true | false |
| share.coordinator.threads | 1 | 5 | false | true | false |
| share.coordinator.write.timeout.ms | 5000 | 5 | false | true | false |
| share.fetch.purgatory.purge.interval.requests | 1000 | 5 | false | true | false |
| socket.connection.setup.timeout.max.ms | 30000 | 5 | false | true | false |
| socket.connection.setup.timeout.ms | 10000 | 5 | false | true | false |
| socket.listen.backlog.size | 50 | 5 | false | true | false |
| socket.receive.buffer.bytes | 102400 | 5 | false | true | false |
| socket.request.max.bytes | 104857600 | 5 | false | true | false |
| socket.send.buffer.bytes | 102400 | 5 | false | true | false |
| ssl.allow.dn.changes | false | 5 | false | true | false |
| ssl.allow.san.changes | false | 5 | false | true | false |
| ssl.cipher.suites |  | 5 | false | false | false |
| ssl.client.auth | none | 5 | false | false | false |
| ssl.enabled.protocols | TLSv1.2,TLSv1.3 | 5 | false | false | false |
| ssl.endpoint.identification.algorithm | https | 5 | false | false | false |
| ssl.engine.factory.class |  | 5 | false | false | false |
| ssl.key.password |  | 5 | false | false | true |
| ssl.keymanager.algorithm | SunX509 | 5 | false | false | false |
| ssl.keystore.certificate.chain |  | 5 | false | false | true |
| ssl.keystore.key |  | 5 | false | false | true |
| ssl.keystore.location |  | 5 | false | false | false |
| ssl.keystore.password |  | 5 | false | false | true |
| ssl.keystore.type | JKS | 5 | false | false | false |
| ssl.principal.mapping.rules | DEFAULT | 5 | false | true | false |
| ssl.protocol | TLSv1.3 | 5 | false | false | false |
| ssl.provider |  | 5 | false | false | false |
| ssl.secure.random.implementation |  | 5 | false | false | false |
| ssl.trustmanager.algorithm | PKIX | 5 | false | false | false |
| ssl.truststore.certificates |  | 5 | false | false | true |
| ssl.truststore.location |  | 5 | false | false | false |
| ssl.truststore.password |  | 5 | false | false | true |
| ssl.truststore.type | JKS | 5 | false | false | false |
| telemetry.max.bytes | 1048576 | 5 | false | true | false |
| transaction.abort.timed.out.transaction.cleanup.interval.ms | 10000 | 5 | false | true | false |
| transaction.max.timeout.ms | 900000 | 5 | false | true | false |
| transaction.partition.verification.enable | true | 5 | false | false | false |
| transaction.remove.expired.transaction.cleanup.interval.ms | 3600000 | 5 | false | true | false |
| transaction.state.log.load.buffer.size | 5242880 | 5 | false | true | false |
| transaction.state.log.min.isr | 2 | 4 | false | true | false |
| transaction.state.log.num.partitions | 50 | 5 | false | true | false |
| transaction.state.log.replication.factor | 3 | 4 | false | true | false |
| transaction.state.log.segment.bytes | 104857600 | 5 | false | true | false |
| transaction.two.phase.commit.enable | false | 5 | false | true | false |
| transactional.id.expiration.ms | 604800000 | 5 | false | true | false |
| unclean.leader.election.enable | false | 5 | false | false | false |
