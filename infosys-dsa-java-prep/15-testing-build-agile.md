# 15 · JUnit, Mockito, Build Tools and Agile 🔴🔴
**Time needed: 60 minutes**

**The job description names all of this explicitly**, and it is the part of the spec your
resume covers most thinly. Your resume lists JUnit but **not Mockito**, and the JD asks for
*"JUnit, Mockito, and unit testing frameworks"*. Close that gap before Saturday — it is the
cheapest marks available this week.

The JD also names **Maven or Gradle**, **Git**, **Agile ceremonies**, **code reviews**,
**technical documentation** and **supporting production deployments**. None of those is
hard. All of them are questions you can lose points on by having nothing to say.

---

# Part A · JUnit and Mockito 🔴🔴

## Q1. Unit test vs integration test

**Say this.**
> "A unit test exercises one class in isolation with its collaborators mocked, so it is fast
> and when it fails you know exactly what broke. An integration test wires real things
> together — the repository against a database, or the controller through the Spring context
> — and tells you the pieces actually fit.
>
> I write mostly unit tests over service logic, because that is where the business rules
> live, plus a smaller number of integration tests over the paths that would be expensive to
> get wrong. What I test is **behaviour and rules**, not lines."

**Real-time example from your own work.** On the card approval workflow, the valuable tests
are not "an approval succeeds". They are the **negative state transitions**: an already
approved application cannot be approved again, a rejected one cannot move back to pending, a
requester cannot approve their own. Those are the rules that cost money, and they are exactly
what a workflow needs tested.

## Q2. 🔴🔴 JUnit 5 — the annotations

```java
class CardApplicationServiceTest {

    @BeforeEach  void setUp()      { }    // before EVERY test
    @AfterEach   void tearDown()   { }
    @BeforeAll static void once()  { }    // once for the class - must be static
    @AfterAll  static void done()  { }

    @Test
    void approvesApplicationWhenAuthoriserIsValid() { }

    @Test @Disabled("pending requirement clarification")
    void skipped() { }

    @ParameterizedTest
    @ValueSource(strings = {"", " ", "  "})
    void rejectsBlankReference(String input) { }
}
```

**JUnit 4 → 5 differences**, in case they ask: `@Before` became `@BeforeEach`, `@BeforeClass`
became `@BeforeAll`, `@RunWith` became `@ExtendWith`, `@Ignore` became `@Disabled`, and
expected exceptions moved from `@Test(expected = …)` to `assertThrows`.

```java
assertEquals(APPROVED, result.getStatus());
assertTrue(result.isComplete());
assertThrows(IllegalStateException.class, () -> service.approve(alreadyApproved));
assertAll(() -> assertEquals(1, a), () -> assertEquals(2, b));   // reports both failures
```

## Q3. 🔴🔴 Mockito — the core of this file

```java
@ExtendWith(MockitoExtension.class)
class CardApplicationServiceTest {

    @Mock  CardApplicationRepository repository;   // database - mock it
    @Mock  NotificationSender notifier;            // external - mock it
    @InjectMocks CardApplicationService service;   // the class under test

    @Test
    void notifiesRequesterOnApproval() {
        CardApplication app = new CardApplication(1L, PENDING);
        when(repository.findById(1L)).thenReturn(Optional.of(app));

        service.approve(1L, "authoriser-7");

        ArgumentCaptor<CardApplication> saved = ArgumentCaptor.forClass(CardApplication.class);
        verify(repository).save(saved.capture());
        assertEquals(APPROVED, saved.getValue().getStatus());
        verify(notifier).send(eq("authoriser-7"), any(Message.class));
    }

    @Test
    void throwsWhenApplicationMissing() {
        when(repository.findById(99L)).thenReturn(Optional.empty());
        assertThrows(ApplicationNotFoundException.class, () -> service.approve(99L, "x"));
        verifyNoInteractions(notifier);          // and nothing was sent
    }
}
```

**The pieces, and what each is for:**

| | What it does |
|---|---|
| `@Mock` | Creates a fake collaborator |
| `@InjectMocks` | Builds the class under test with the mocks injected |
| `@Spy` | Wraps a **real** object — most calls real, some stubbed |
| `@MockBean` | The Spring version: replaces a bean in the application context |
| `when(x).thenReturn(y)` | Stub the input |
| `when(x).thenThrow(e)` | Stub a failure |
| `verify(mock).method()` | Assert the interaction happened |
| `verify(mock, times(2))` | …this many times. Also `never()`, `atLeastOnce()` |
| `verifyNoInteractions(mock)` | Assert nothing was called on it |
| `ArgumentCaptor` | Capture **what** was passed, to assert on it |
| `any()`, `eq()` | Argument matchers — if you use one, use them for all arguments |

**Say this.**
> "I mock what I do not own or what would make the test slow and non-deterministic —
> repositories, external clients, anything over the network. I do not mock the class under
> test, and I try not to mock simple value objects, because then the test just asserts my own
> mock setup back at me.
>
> `when(...).thenReturn(...)` sets up the input and `verify(...)` checks an interaction
> actually happened, which matters when the important outcome is a side effect rather than a
> return value. `ArgumentCaptor` is what I reach for when I need to assert on what was
> passed, not just that something was."

### 🔴 The questions they follow up with

**"Mock vs stub?"**
> "A stub just returns canned answers so the test can proceed. A mock also records how it was
> called, so you can verify the interaction. Mockito does both, which is why the words get
> used loosely."

**"What can Mockito not mock?"** Historically `static` and `final` methods and private
methods — `mockito-inline` handles statics now, but the better answer is that needing to
mock a static is usually a design smell, because it means the dependency is not injectable.

**"How do you test a void method?"** You cannot assert a return value, so you verify the
interaction — `verify(repository).delete(entity)` — or capture and assert on the argument.

**"How do you stub a void method to throw?"** `doThrow(ex).when(mock).method();` — the
`doX().when()` form, because `when(mock.voidMethod())` will not compile.

## Q4. Testing a Spring Boot application

```java
@WebMvcTest(CardController.class)         // controller layer only - fast
class CardControllerTest {
    @Autowired MockMvc mockMvc;
    @MockBean CardApplicationService service;

    @Test void returns404WhenMissing() throws Exception {
        when(service.findById(1L)).thenThrow(new ApplicationNotFoundException(1L));
        mockMvc.perform(get("/api/cards/1")).andExpect(status().isNotFound());
    }
}
```
- `@SpringBootTest` loads the whole context — integration, slow.
- `@WebMvcTest` / `@DataJpaTest` load one slice — much faster.
- `@MockBean` swaps a real bean for a mock inside the context.

**Say why slices matter:** "A fast suite is one people actually run. If every test boots the
whole application, the suite gets skipped, and a skipped suite protects nothing."

## Q5. Coverage — the answer that shows judgement
> "Coverage tells you what was **executed**, not what was **verified** — a test with no
> assertion still counts towards it. So I would rather have the critical paths genuinely
> tested than chase a percentage. That said, a very low number is a useful warning sign, and
> a quality gate on new code in the pipeline is a reasonable safety net."

## Q6. 🔴 If they ask how much Mockito you have used — be honest

Your resume says JUnit, not Mockito. If the question is direct:

> "I have written JUnit unit and integration tests for REST APIs and workflow logic, and
> validated them through SIT and UAT. My mocking has been lighter than my JUnit usage, so I
> would not overstate it — but I understand the model: mock the collaborators you do not own,
> stub with `when/thenReturn`, verify interactions, and capture arguments when you need to
> assert on what was passed."

**Then show it** using the example above. That answer is completely respectable at your
level. Claiming deep Mockito and then fumbling `doThrow` on a void method is not.

---

# Part B · Build tools and Git

## Q7. Maven — what they will actually ask
> "Maven is a build and dependency management tool driven by `pom.xml`. It resolves
> dependencies transitively from a repository, and it defines a standard lifecycle so any
> Maven project builds the same way."

**The lifecycle, in order** — worth knowing:
`validate → compile → test → package → verify → install → deploy`

- `mvn clean install` — the one everybody runs. Wipes `target/`, builds, runs tests, and
  puts the artefact in your **local** repository.
- `mvn package` — builds the JAR but does not install it locally.
- `mvn test` — compiles and runs tests only.

**Scopes:** `compile` (default), `provided` (available at compile, supplied at runtime —
e.g. a servlet API), `runtime`, `test` (JUnit, Mockito).

**Two things worth mentioning unprompted:**
- **The parent POM.** `spring-boot-starter-parent` manages versions, which is why you add
  `spring-boot-starter-web` with no version and get a compatible set.
- **Dependency conflicts.** Maven resolves to the **nearest** version in the tree, which is
  how you end up with a version you did not ask for. `mvn dependency:tree` is how you find
  it; `<dependencyManagement>` or an exclusion is how you pin it. Saying this signals real
  build experience.

**Maven vs Gradle:** Maven is XML and convention-driven, predictable and verbose. Gradle uses
a Groovy or Kotlin DSL, is more flexible, and is faster on large builds thanks to incremental
builds and a build cache. You use Maven; say so, and say you could pick up Gradle.

## Q8. Git — the likely questions
- **merge vs rebase** — merge preserves history and adds a merge commit; rebase replays your
  commits on top for a linear history. **Never rebase a shared branch**, because it rewrites
  commits other people already have.
- **`git pull` = `fetch` + `merge`.** `fetch` alone just updates your remote-tracking
  branches, which is the safe way to look before you leap.
- **Resolving a conflict** — understand both sides rather than picking one. In business logic,
  taking one blindly silently drops someone's work.
- **`revert` vs `reset`** — `revert` makes a new commit undoing an old one, safe on a shared
  branch. `reset` moves the branch pointer and rewrites history, so it is for local work only.
- **`cherry-pick`** — apply one commit onto another branch, typically a hotfix.
- **Branching** — feature branch, pull request, reviewed before merge. You used Bitbucket and
  Bamboo, so say that.

---

# Part C · Agile, documentation and deployment

The JD lists these explicitly, so have a sentence for each.

## Q9. The ceremonies — what each is actually for

| Ceremony | Purpose | The honest thing to say |
|---|---|---|
| **Sprint planning** | Agree what the team commits to | "This is where ambiguity should be caught — if a story is not clear enough to estimate, it is not ready" |
| **Daily stand-up** | Surface blockers, not a status report | "The useful part is the blockers. If it turns into a status recital it stops being worth the time" |
| **Sprint review** | Show working software to stakeholders | "Demoing to the BA and product owner is where you find out you built the wrong thing — better then than in UAT" |
| **Retrospective** | Improve the process | "The value is only in the actions. A retro with no action items is a complaint session" |
| **Refinement** | Size and clarify upcoming work | "Where most estimation problems get solved, before anything is committed" |

**Say this if asked generally:**
> "We worked two-week sprints with stand-ups, refinement, review and retro, tracked in Jira.
> The ceremony I found most valuable was refinement, because that is where an unclear
> requirement gets caught — before someone has spent three days building the wrong thing."

## Q10. "Analyse business requirements and translate them into technical solutions"
Straight from the JD's responsibilities. It is really a question about handling ambiguity.

> "I do not start building on an assumption I have not confirmed. I write down what I have
> understood including the gaps, then go back with **specific** questions and a proposed
> default for each, rather than asking someone to clarify. A specific question is much faster
> to answer and it gets the decision recorded.
>
> On the recall workflow there were states where it was not defined who could act. I listed
> the cases, proposed a default for each, and asked the BA to confirm. That was a short call
> instead of a long email thread."

## Q11. Technical documentation
> "API documentation that lives with the code, so it does not drift — we used Swagger, so the
> contract is generated from the code rather than maintained separately. Beyond that, a short
> design note for anything non-obvious, and runbook-style notes for operational things. My
> test is whether someone else could pick up my work if I were not there."

## Q12. Supporting production deployments
> "We released through Bamboo CI/CD after SIT and UAT sign-off. What I would do around a
> release: validate the deployment in the environment rather than assuming it worked, watch
> the logs and error rates for the first period after it goes out, and know what the rollback
> is **before** you deploy, not while something is failing.
>
> Database changes need particular care, which is why we used Liquibase — versioned
> migrations mean the schema change is repeatable and reviewable rather than someone running
> a script by hand."

That Liquibase point is a genuinely strong one and it is on your resume. Use it.

## Q13. Cloud platforms — the JD mentions integration, be honest
Your resume has Docker but not a cloud platform.

> "I have worked with Docker in the development setup, and our deployments went through
> Bamboo, but I have not owned cloud infrastructure — so I would call that exposure rather
> than depth. I understand the model: the application is containerised and configuration
> comes from the environment rather than the artefact, which is what lets the same build be
> promoted from SIT to UAT to production."

That last sentence shows you understand the principle even without the platform experience,
which is what they are actually probing.

---

## ✅ Check yourself before moving on
1. Write the Mockito test from memory — `@Mock`, `@InjectMocks`, `when`, `verify`, captor.
2. `doThrow(...).when(mock).method()` — and **why** `when(mock.voidMethod())` will not compile.
3. The Maven lifecycle in order, and what `mvn clean install` does.
4. merge vs rebase, and why you never rebase a shared branch.
5. What each Agile ceremony is for, in one sentence each.
6. Your honest Mockito answer, and your honest cloud answer.
