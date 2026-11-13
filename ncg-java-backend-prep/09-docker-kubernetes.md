# 09 · Docker, Kubernetes and Containerisation 🔴🔴
**Time needed: 90 minutes**

**This is your biggest gap against this job description, and it is named three times** —
*"Docker, Kubernetes, Containerization"* in the required skills, *"familiarity with
containerization technologies"* in the ideal-candidate list, and *"support DevOps practices"*
in the responsibilities.

**Your resume does not mention any of it.** So the goal of this file is not to pretend — it is
to understand the model well enough to hold a sensible conversation, and to say honestly where
your hands-on ends. At 2 years, nobody expects you to run a cluster. They expect you to know
what a container is and why your Spring Boot service is put in one.

> **🔴 The answer that protects you all day:**
> *"I have not owned the container or deployment side — our platform was deployed by a
> separate team. So I would call that understanding rather than hands-on. What I do know is
> the model and why it is used, and I have built the applications that go inside the
> containers."*
>
> Say that **before** they probe, not after. Naming the boundary first makes everything else
> you say credible.

---

## Part A · Docker

### First, the context: what problem does a container solve?

The oldest complaint in software: **"it works on my machine."**

Your application needs a particular Java version, particular environment variables, a
particular OS library. The server has slightly different ones. It works in SIT and fails in
UAT, and you lose a day finding out why.

A **container** packages the application **together with everything it needs to run** — the
JRE, the libraries, the configuration — into one image. That image runs identically wherever
there is a container runtime. The machine underneath stops mattering.

### Container vs virtual machine — a near-certain question

```
   VIRTUAL MACHINES                      CONTAINERS
 ┌──────────┬──────────┐              ┌──────────┬──────────┐
 │  App A   │  App B   │              │  App A   │  App B   │
 │  Guest   │  Guest   │  ← a FULL    │   libs   │   libs   │
 │    OS    │    OS    │     OS each  ├──────────┴──────────┤
 ├──────────┴──────────┤              │  Container runtime  │
 │     Hypervisor      │              ├─────────────────────┤
 ├─────────────────────┤              │      Host OS        │  ← ONE shared kernel
 │      Host OS        │              ├─────────────────────┤
 ├─────────────────────┤              │      Hardware       │
 │      Hardware       │              └─────────────────────┘
```

> "A virtual machine includes a whole guest operating system, so it is heavy — gigabytes, and
> a minute or more to boot. A container shares the host's kernel and packages only the
> application and its dependencies, so it is tens or hundreds of megabytes and starts in
> seconds. The trade-off is isolation: VMs isolate more strongly because they do not share a
> kernel. For running many instances of the same service, containers win on density and start-up
> time, which is what makes auto-scaling practical."

### The three words you must not mix up

| Term | What it is | The analogy |
|---|---|---|
| **Dockerfile** | The recipe — text instructions to build the image | The recipe |
| **Image** | The built, read-only package | The cake you baked |
| **Container** | A running instance of an image | A slice being eaten |

**One image, many containers.** That is the whole point — the same image runs in SIT, UAT and
production, and you scale by running more containers from it.

### A Dockerfile for a Spring Boot app — know roughly what it looks like

```dockerfile
# multi-stage build: stage 1 compiles, stage 2 only carries the result
FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline        # cached layer - deps rarely change
COPY src ./src
RUN mvn clean package -DskipTests

FROM eclipse-temurin:17-jre-alpine   # small runtime image, no Maven, no JDK
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**Two things here are worth understanding, because they are what an interviewer asks about:**

**1. Why a multi-stage build?** The first stage needs Maven and the full JDK to compile — about
700MB of tooling. The final image needs none of that, only the JRE and the JAR. Multi-stage
means the build tools are thrown away and the shipped image is a fraction of the size. Smaller
image means faster pulls, faster deploys, and a smaller attack surface.

**2. Why copy `pom.xml` and download dependencies before copying `src`?** Because **Docker
caches each instruction as a layer**. Dependencies change rarely; source changes constantly. If
you copy everything at once, every code change re-downloads every dependency. Split like this,
the dependency layer is reused and the rebuild is seconds instead of minutes.

**That layer-caching answer is the single best thing you can say about Docker**, because it
shows you understand how images are actually built rather than having copied a file.

### The commands to recognise

```bash
docker build -t recall-service:1.2 .     # build an image from the Dockerfile here
docker run -p 8080:8080 recall-service   # run it, mapping host port -> container port
docker ps                                # what is running
docker logs -f <container>               # follow the logs - your tail -f equivalent
docker exec -it <container> sh           # get a shell inside a running container
docker images                            # what images exist locally
```

`-p 8080:8080` is **host port : container port**. The container has its own network namespace,
so without the mapping nothing on the host can reach it.

### Configuration — the point that connects to Spring Boot
> "The image must be the same in every environment, so the environment-specific parts cannot
> be baked into it. Database URLs, credentials and feature flags come in as **environment
> variables** at run time. That maps directly onto Spring Boot profiles and
> `application.yml` — the same artefact is promoted from SIT to UAT to production and only
> the configuration changes. That is the real discipline containers enforce."

**And never put secrets in an image.** Anyone who can pull it can read every layer.

---

## Part B · Kubernetes

### First, the context: what problem does Kubernetes solve?

Docker runs **one container on one machine**. Now run 40 services, three replicas each, across
a dozen machines. Something has to decide which machine each container runs on, restart the
ones that die, replace them during a release without downtime, and give them stable addresses
when their IPs keep changing.

**That is orchestration, and Kubernetes is the orchestrator.** The word to use is
*declarative*: you describe the desired state — "I want three replicas of this image" — and
Kubernetes continuously works to make reality match. If a pod dies, it starts another, because
reality stopped matching the declaration.

### The objects you must be able to name

| Object | What it is |
|---|---|
| **Pod** | The smallest unit — usually one container. **Pods are disposable** and get a new IP each time |
| **ReplicaSet** | Keeps N copies of a pod running |
| **Deployment** | Manages ReplicaSets; this is what gives you rolling updates and rollback |
| **Service** | A **stable** name and IP in front of changing pods, with load balancing |
| **Ingress** | Routes outside HTTP traffic to Services — host and path based |
| **ConfigMap** | Non-secret configuration injected as env vars or files |
| **Secret** | The same, for sensitive values (base64 encoded, not encrypted by default) |
| **Namespace** | A logical partition of the cluster — dev, SIT, UAT |

### 🔴 The question they will actually ask: "Why do you need a Service?"
> "Because pods are disposable. Every time a pod is replaced it gets a new IP, so nothing can
> depend on a pod's address. A Service gives a stable DNS name and IP, and load balances across
> whichever pods are currently healthy. So one service calls another by name — `http://recall-service`
> — and Kubernetes resolves it, exactly the role Eureka played in my Classifieds project."

**That connection is strong** — it ties a named requirement to something you actually built.

### A Deployment, roughly
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: recall-service
spec:
  replicas: 3
  template:
    spec:
      containers:
        - name: recall-service
          image: registry/recall-service:1.2
          ports: [{ containerPort: 8080 }]
          env:
            - name: SPRING_PROFILES_ACTIVE
              value: uat
          readinessProbe:                  # is it ready for traffic yet?
            httpGet: { path: /actuator/health/readiness, port: 8080 }
          livenessProbe:                   # is it still alive, or should it be restarted?
            httpGet: { path: /actuator/health/liveness, port: 8080 }
          resources:
            requests: { memory: "512Mi", cpu: "250m" }
            limits:   { memory: "1Gi",   cpu: "500m" }
```

### 🔴🔴 Probes — the best Kubernetes answer available to a Spring Boot developer
This is where your actual knowledge connects, because **Spring Boot Actuator provides these
endpoints**.

> "**Readiness** asks 'can this pod take traffic yet?' A Spring Boot service takes time to
> start — context initialisation, the connection pool, Liquibase migrations. Until readiness
> passes, Kubernetes keeps it out of the Service's load balancing, so no request hits a service
> that is not ready.
>
> **Liveness** asks 'is this still alive?' If it fails repeatedly, Kubernetes restarts the pod.
>
> Getting them the wrong way round is a classic production incident: if a slow startup fails a
> *liveness* probe, Kubernetes keeps killing and restarting the pod and it never comes up."

**That last sentence is a real, specific failure mode, and it will land well.**

### Rolling updates and rollback
> "A Deployment replaces pods gradually rather than all at once — it brings up new ones, waits
> for readiness, then takes old ones down. So there is no downtime, and if the new version
> fails readiness the rollout stops rather than taking the service down. `kubectl rollout
> undo` goes back to the previous version.
>
> The thing that has to be true for this to work is that **both versions run at the same time
> for a period**. So a database migration has to be backwards compatible — add a nullable
> column, deploy, then use it. That is the same expand-then-contract discipline we used with
> Liquibase."

**That is an excellent answer** — it takes a Kubernetes question and answers it with something
you genuinely did.

### Scaling
`kubectl scale deployment recall-service --replicas=5`, or a **HorizontalPodAutoscaler** that
adds pods when CPU or memory passes a threshold.
**The prerequisite to mention:** the service has to be **stateless** for this to work. Any
session state must live outside the pod — in a database or a cache — because the next request
may land on a different pod. That is the same reason Spring beans should be stateless, and the
same reason a JWT suits this architecture better than a server-side session.

### The commands to recognise
```bash
kubectl get pods                      # what is running
kubectl describe pod <name>           # why is it not running - events are at the bottom
kubectl logs -f <pod>                 # follow the logs
kubectl logs <pod> --previous         # logs of the crashed instance - this is the one for CrashLoopBackOff
kubectl exec -it <pod> -- sh          # shell inside
kubectl rollout undo deployment/<name>
```

**Two statuses to recognise**, because they come up as scenario questions:
- **CrashLoopBackOff** — the container keeps starting and dying. Check `logs --previous`;
  usually a missing environment variable, a database it cannot reach, or a failed migration.
- **ImagePullBackOff** — it cannot fetch the image. Wrong tag, or registry credentials missing.

---

## ✅ Check yourself before moving on
1. Container vs VM, including the isolation trade-off.
2. Dockerfile vs image vs container, and **why layer caching means you copy `pom.xml` first**.
3. Why a Service exists — and the Eureka comparison.
4. Readiness vs liveness, and the failure that happens when you confuse them.
5. Why rolling updates force backwards-compatible database migrations.
6. **Your honest boundary statement**, said before they have to ask for it.
