# 13 · Testing, Code Review and Engineering Practice 🔴🔴
**Time needed: 60 minutes**

**This file is where you can look better than your years.** Most candidates at 1–2 years
prepare Java and Spring and nothing else. Your resume leads with JUnit 5, Mockito,
SonarQube, code review, logging and root cause analysis — and a bank cares about all of it,
because in a regulated environment the *way* code gets built is part of the product.

---

# Part A · Testing

## Q1. 🔴🔴 Unit test vs integration test — and what you actually test

**Say this.**
> "A unit test exercises one class in isolation with its collaborators mocked, so it is fast
> and tells you exactly what broke. An integration test wires real components together —
> the repository against a database, or the controller through the full Spring context — and
> tells you that the pieces actually fit.
>
> I write mostly unit tests over service logic, because that is where the business rules
> live, plus a smaller number of integration tests over the paths that would be expensive to
> get wrong. What I aim to test is **behaviour and rules**, not lines — the negative cases
> especially, because those are the ones that cost money."

**Real-time example.** On a payment flow the valuable tests are not "a successful payment
succeeds". They are: a payment below the minimum is rejected, a duplicate request does not
debit twice, a vendor timeout leaves the transaction in a recoverable state rather than an
unknown one. Those are the rules; the happy path mostly tests itself in QA.

## Q2. 🔴🔴 Mockito — what you mock and why

```java
@ExtendWith(MockitoExtension.class)
class PaymentServiceTest {

    @Mock  PaymentVendorClient vendorClient;     // external - always mock
    @Mock  TransactionRepository repository;     // database - mock in a unit test
    @InjectMocks PaymentService service;         // the thing under test

    @Test
    void marksTransactionFailedWhenVendorRejects() {
        when(vendorClient.initiate(any())).thenReturn(VendorResponse.rejected("INSUFFICIENT"));

        service.process(new PaymentRequest("acc-1", new BigDecimal("100.00")));

        ArgumentCaptor<Transaction> saved = ArgumentCaptor.forClass(Transaction.class);
        verify(repository).save(saved.capture());
        assertThat(saved.getValue().getStatus()).isEqualTo(FAILED);
        verifyNoMoreInteractions(vendorClient);
    }
}
```

**Say this.**
> "I mock the things I do not own or that make the test slow and non-deterministic —
> external vendor clients, repositories, anything over the network. I do not mock the class
> under test, and I try not to mock value objects, because then the test is just asserting
> my own mock setup.
>
> `when(...).thenReturn(...)` sets up the input; `verify(...)` checks an interaction actually
> happened, which matters when the important outcome is a side effect rather than a return
> value. `ArgumentCaptor` is what I use when I need to assert on *what* was passed, not just
> that something was."

**Know these terms:** `@Mock` creates the double, `@InjectMocks` builds the class under test
with the mocks injected, `@Spy` wraps a real object so most calls are real, and `@MockBean`
is the Spring version that replaces a bean in the application context.

**The trap question — "what is the difference between a mock and a stub?"**
> "A stub just returns canned answers so the test can proceed. A mock also records how it was
> called, so you can verify the interaction. Mockito does both, which is why people use the
> words loosely."

## Q3. "What is a good test?" and the coverage question

**Say this.**
> "A good test fails for exactly one reason, and the name tells you what broke without
> reading the body. I name them as behaviour — `marksTransactionFailedWhenVendorRejects` —
> rather than `testProcess1`.
>
> On coverage: it tells you what was *executed*, not what was *verified*. A test with no
> assertion still counts towards it. So I would rather have the critical paths genuinely
> covered than chase a number — though a very low number is still a useful warning sign, and
> a gate in the pipeline is a reasonable safety net."

**Arrange, Act, Assert** is worth naming as the structure you write them in.

## Q4. TDD — have an honest opinion
> "I have not worked strictly test-first, so I would not claim to be a TDD practitioner. What
> I do find genuinely useful is writing the test for a bug **before** fixing it, because that
> proves you have actually reproduced it and it stops the bug coming back."

That is honest, it is true of almost everyone, and the second sentence shows you have
thought about why the practice exists.

---

# Part B · Code review and code quality

## Q5. 🔴 "What do you look for in a code review?"

**Say this — in this order, because the order is the answer.**
> "First **correctness**: does it do what the ticket says, and are the edge cases handled —
> nulls, empty results, boundaries. Second **error handling**: is anything being swallowed
> silently, which is the worst outcome because the failure becomes invisible.
>
> Then the **data layer**, because that is where the expensive problems hide — a query
> inside a loop, a missing index, `@Transactional` on the wrong method. Then **tests** — not
> the count, whether the meaningful cases are covered. Then **security** — is input validated,
> is authorisation checked server side, is anything sensitive being logged. And **readability**
> last: naming, method length, duplication. It matters, but I would not block a change on it
> alone."

**On giving feedback:**
> "I separate what must change from what is a suggestion and say which is which, because
> 'this could be better' just wastes the author's time. I ask rather than instruct when I do
> not know the context. And if a thread goes past three replies I go and talk to them, because
> that usually means we are misunderstanding each other rather than disagreeing."

## Q6. SonarQube and static analysis

**Say this.**
> "SonarQube runs static analysis in the pipeline and reports bugs, vulnerabilities, code
> smells, duplication and coverage. The value is that it catches the mechanical things — an
> unclosed resource, a possible null dereference, a hardcoded credential — so that human
> review can spend its time on design and correctness instead.
>
> The thing to be careful about is treating every finding as equally important. A genuine
> vulnerability and a slightly long method are both 'issues' in the report and are not
> remotely the same, so it needs judgement rather than driving the count to zero."

**Quality gate** is the term worth knowing: a threshold in the pipeline that fails the build
if new code drops below the standard — often applied to *new* code only, so an existing
codebase can improve without blocking everything.

## Q7. Logging and observability

**Say this.**
> "I improved the logging on Tradu specifically so issues were faster to diagnose. The
> principles I would apply: log at the boundaries — incoming request, outgoing vendor call,
> and the result — so you can see where a flow stopped. Include an identifier that lets you
> trace one transaction through the logs. Use levels properly, so ERROR means something
> needs attention rather than being noise.
>
> And **never log sensitive data** — card numbers, credentials, personal details. In a
> regulated environment that is a compliance breach, not a style problem. That is the part I
> would check in review."

**If asked about production support:** logs first, then what changed recently, then reproduce.
Form a hypothesis and confirm it before fixing, because fixing the wrong thing hides the real
problem.

---

# Part C · Delivery

## Q8. Git and branching

**Say this.**
> "Feature branches off the main line, small commits with messages that say why rather than
> what, and a pull request reviewed before merge. I rebase my own branch to keep history
> readable but I would not rewrite history on a shared branch. Merge conflicts I resolve by
> understanding both changes rather than picking a side — in business logic, taking one
> blindly silently drops someone's work."

## Q9. CI/CD, honestly at your level

**Say this.**
> "I worked within a Jenkins pipeline rather than owning it. What I understand is the shape:
> a commit triggers a build, the unit tests run, SonarQube analysis runs against the quality
> gate, and an artefact is produced and deployed to an environment. The point is that the
> same artefact is promoted rather than rebuilt per environment, so what was tested is what
> ships.
>
> I would not claim to have built pipelines from scratch, but I am comfortable working in one
> and fixing my own build failures."

Calibrated honesty. Do not claim to have built the pipeline.

## Q10. Agile in practice
> "Two-week sprints, stand-ups, JIRA for tracking, and refinement where we sized the work. The
> part I found most useful was refinement, because that is where ambiguity in a ticket gets
> caught — before someone has built the wrong thing."

**If asked about estimation:** break it down until you can picture doing each piece, include
testing and review time, and **state your assumptions** so a changed assumption is a
re-estimate rather than a missed deadline.

---

## Q11. 🔴 Secure coding — worth having for a bank

Even a short answer here is unusual at your level and it lands well.

> "The basics I would always check: validate input at the boundary and never trust the
> client; use parameterised queries or JPA rather than string-concatenated SQL, which is how
> injection happens; enforce authorisation server side on every endpoint, not in the UI;
> never log or expose sensitive data; and keep secrets out of code and configuration in the
> repository — environment variables or a secrets manager.
>
> And return generic error messages to the client while logging the detail internally, because
> a stack trace tells an attacker about your framework versions and internal structure."

---

## ✅ Check yourself before moving on
1. What you mock and what you do not, and why.
2. Write the Mockito test above from memory — `@Mock`, `@InjectMocks`, `when`, `verify`.
3. What you look for in a code review, **in order**.
4. The coverage answer — what it measures and what it does not.
5. Three secure coding practices, without prompting.
