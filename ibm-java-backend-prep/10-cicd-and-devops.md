# 10 · CI/CD and DevOps 🔴
**Time needed: 45 minutes**

The JD names **Jenkins, GitHub Actions and Azure DevOps**, and lists *"Implement CI/CD
pipelines and support DevOps practices"* as a responsibility.

**Your resume does not mention any pipeline tool.** But you have been through SIT and UAT
release cycles and done deployment validation, so you have lived inside a release process even
if you did not own the pipeline. **That is the honest and sufficient answer at your level.**

> **🔴 The boundary statement:**
> *"I worked inside the release process rather than owning the pipeline — our builds and
> deployments went through SIT and UAT cycles, and I did the deployment validation after a
> release. So I understand the shape of it and I am comfortable working in one, but I have not
> built a pipeline from scratch."*

---

## First, the context: what CI and CD actually mean

**Continuous Integration (CI)** — every commit is automatically built and tested. The point is
to find out within minutes that something broke, instead of at the end of a sprint when ten
people's changes are tangled together.

**Continuous Delivery (CD)** — every build that passes is automatically turned into a
deployable artefact and pushed to an environment. Delivery means it is *ready* to release;
**Continuous Deployment** means it goes to production automatically with no human gate.

In BFSI, the last step almost never happens automatically — production releases are gated and
approved, because the environment is regulated. **Say that if asked; it shows you understand
the context rather than reciting the textbook.**

## The pipeline shape — this is what you need to know, whatever the tool

```
  commit
    │
    ▼
  BUILD        mvn clean package      compile, run unit tests
    │
    ▼
  TEST         integration tests, code coverage
    │
    ▼
  QUALITY      static analysis, security scan, coverage gate
    │
    ▼
  PACKAGE      build the Docker image, tag it, push to a registry
    │
    ▼
  DEPLOY       SIT  →  UAT  →  (approval)  →  PROD
```

### 🔴 The principle that matters most
> "**The same artefact is promoted through the environments.** You build once, and that exact
> image moves from SIT to UAT to production — only the configuration changes, through
> environment variables. If each environment rebuilt from source you would be testing one thing
> and shipping another, and 'it passed in UAT' would mean nothing."

That is the single best sentence you can say about CI/CD, and it ties straight back to the
container discipline in file 09.

## The three tools, in one line each

| Tool | What it is |
|---|---|
| **Jenkins** | The long-established one. Self-hosted, plugin-driven, pipelines written as a `Jenkinsfile` in Groovy. Very flexible, and you maintain the server yourself. |
| **GitHub Actions** | Built into GitHub. YAML workflows in `.github/workflows/`, triggered by events — push, pull request, schedule. Hosted runners, no server to maintain. |
| **Azure DevOps** | Microsoft's suite — Repos, Pipelines, Boards, Artifacts. YAML pipelines. Common in enterprises already on Azure. |

**They do the same job.** If asked which you prefer, the honest answer is better than a
preference you cannot defend:
> "I have worked within a pipeline rather than choosing the tool. They all express the same
> shape — build, test, quality gate, package, deploy. Jenkins is the most flexible and the most
> to maintain; GitHub Actions is the simplest if the code is already on GitHub; Azure DevOps
> makes sense in a Microsoft shop. I would be comfortable picking up any of them."

## Know roughly what a pipeline file looks like

```yaml
# GitHub Actions
name: build
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: { java-version: '17', distribution: 'temurin', cache: 'maven' }
      - run: mvn clean verify                    # compile + unit + integration tests
      - run: docker build -t registry/recall:${{ github.sha }} .
```

**Two details worth noticing**, because they are what someone asks about:
- **`cache: 'maven'`** — the dependency cache, for the same reason as Docker layer caching:
  without it every build re-downloads the world.
- **Tagging the image with the commit SHA** — so every deployed artefact traces back to exactly
  one commit. In a regulated environment that traceability is not optional.

## Quality gates
> "A gate fails the build if new code drops below a standard — coverage, static analysis
> findings, or a security scan on dependencies. The one I would always want is a **dependency
> vulnerability scan**, because in BFSI a known CVE in a transitive dependency is a real audit
> finding, not a nice-to-have."

**On coverage as a gate:** it measures what was *executed*, not what was *verified* — a test
with no assertion still counts. Useful as a floor, not as a target.

## Deployment strategies — recognise the names

| Strategy | How it works |
|---|---|
| **Rolling** | Replace instances gradually. The Kubernetes default. |
| **Blue-green** | Two identical environments; switch traffic over at once. Instant rollback, double the infrastructure. |
| **Canary** | Send a small share of traffic to the new version first, watch the error rate, then widen. |

**The constraint they all share**, and the one worth saying: for any of these, **two versions
run at the same time for a while** — so database changes must be backwards compatible. Add a
nullable column, deploy, then use it; remove it only in a later release. That is the
**expand-then-contract** rule, and it is exactly what Liquibase-style versioned migrations are
for.

## Rollback
> "The first question before any release is what the rollback is, decided **before** deploying
> rather than during an incident. With Kubernetes that is `kubectl rollout undo`. The part that
> does not roll back cleanly is the database, which is why migrations need to be additive and
> backwards compatible — you can redeploy the old code, but you cannot un-drop a column."

## Your honest material — use it
You genuinely have this, so say it:
- **SIT and UAT release cycles** — a real gated process, with QA validating before promotion.
- **Deployment validation** — checking the release actually worked in the environment rather
  than assuming it did.
- **Code reviews** as a gate before merge.
- **Production incident resolution** — analysing logs and execution plans, finding root cause,
  coordinating the fix with QA. That is the "support production releases" line in the JD.

## 12-factor ideas worth naming
Two of the twelve are enough, and both connect to things you know:
- **Configuration comes from the environment**, not from the artefact — so one build runs
  everywhere.
- **Services are stateless and disposable** — so any instance can be killed or replaced, which
  is what makes scaling and rolling updates possible. Same reason Spring beans are stateless
  and a JWT beats a server-side session.

---

## ✅ Check yourself before moving on
1. CI vs CD vs continuous deployment — and why BFSI usually gates the last one.
2. **Build once, promote the same artefact** — and why rebuilding per environment is wrong.
3. The pipeline stages in order.
4. Blue-green vs canary vs rolling, and the backwards-compatible migration rule they share.
5. Your boundary statement, said before you are asked for it.
