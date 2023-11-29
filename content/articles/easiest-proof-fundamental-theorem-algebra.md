title: (Possibly) the Easiest Proof of the Fundamental Theorem of Algebra
slug: possibly-easiest-proof-fundamental-theorem-algebra
summary: I'll show you what I think may be the easiest proof of the Fundamental Theorem of Algebra
header_cover: /images/a_working_mathematician.png
tags: math


<style>
.intro-header {
    background-position: 0 -365px;
}
</style>

# Introduction
Back when I first took complex analysis in graduate school, I thought the quick
proof of the Fundamental Theorem of Algebra using Liouville's theorem was pretty
cool. Of course, I was young, and I had a new toy to play with, so, *obviously*
I got a kick out of being able to prove a Fundamental Theorem with some
extremely simple machinery.

No, really. Liouville's theorem is literally something one would expect to see
in about chapter 2 of any [decent
textbook](https://mccuan.math.gatech.edu/courses/6321/lars-ahlfors-complex-analysis-third-edition-mcgraw-hill-science_engineering_math-1979.pdf)
on complex analysis. And, sure enough, if you skip to the second chapter in
Ahlfors, there it is, right after Cauchy's integral formula, from which it
directly follows, on p. 122.

When I say it's "simple machinery," what I mean is that it doesn't really *say*
very much. In full, Liouville's theorem says that "A bounded entire function is
constant." That's something that *sounds* a lot more deep and interesting than
it actually is. All it really means in the grand scheme of things is that all
interesting complex-valued functions (*i.e.* those that are analytic on all of
$\mathbb{C}$ and take on more than one value) will eventually veer off to 
infinity at some point on their domain.[^1]

# Proof using Liouville's theorem

I guess I'm still kind of enamored of this proof, because before I dismiss it, I
want to show it to you. It really is quite neat, and even a little surprising
the first time you see it.  Besides, if I'm going to show you my *new* favorite
proof, I should probably show you my *old* favorite proof for comparison's sake.

Once you've gone through the effort of proving Liouville's theorem, the argument
that establishes the Fundamental Theorem of Algebra is so short, it's almost
anticlimactic. Since it *is* so short, any one version is really just as good as
any other, so I'll just quote the one on p. 122 of Ahlfors:

> Liouville's theorem leads to an almost trivial proof of the *fundamental
theorem of algebra.* Suppose that $P(z)$ is a polynomial of degree $> 0.$ If
$P(z)$ were never zero, the function $1/P(z)$ would be analytic in the whole
plane. We know that $P(z) \to \infty$ for $z \to \infty$, and therefore $1/
P(z)$ tends to zero. This implies boundedness (the absolute value is continuous
on the Riemann sphere and has thus a finite maximum), and by Liouville's theorem
$1/P(z)$ would be constant. Since this is not so, the equation $P(z) = 0$ must
have a root.

Pretty slick, huh?

## Why I don't like that proof anymore

Liouville's theorem is a corollary of the Cauchy integral formula. Don't get me
wrong --- Cauchy's integral formula is a fine theorem and all, but it's also a
[really big
hammer,](https://en.wikipedia.org/wiki/Cauchy%27s_integral_formula#Consequences)
when we can use a tool more appropriate to the job. I prefer to sneak up on a
theorem rather than drop a nuclear bomb on it whenever feasible. It's just more
interesting that way.

## So, whaddaya gonna do about it, huh?

Fine. You got me.

I'm going to give a proof of the Fundamental Theorem of Algebra based on some
much more primitive, topological properties of $\mathbb{C}.$ Even better, we're
gonna use a really wimpy sounding theorem that you see at the end of a first
semester calculus class: the *extreme value theorem.*  As a result, the proof I
give here should be intelligible to anyone who remembers taking calc 1 as an
undergrad.

# Tools needed for the proof

As I mentioned earlier, we don't need a ton of sophisticated theory to make this
proof work. The Extreme Value Theorem, plus a little intuition from calc 1 is
just about it.

## The extreme value theorem

If you studied calculus or real analysis in high school or college, you probably
don't even remember seeing the extreme value theorem. It's kind of like the
Gerald Ford of real analysis theorems. People forget he was even President
sometimes, just like it's easy to forget you ever saw the EVT.

The EVT comes in several sizes and colors, corresponding to where and how one
can expect to see it used. The simplest version is this seemingly not very
interesting little theorem one would typically see in a first semester calculus
course:

**Theorem:** Let $f$ be continuous on $[a,b].$ Then, $f$ attains a maximum and a
minimum value on $[a, b].$

In its final evolution, it looks more like this:

**Theorem:** Let $f : X \to Y$ be continuous, where $Y$ is an ordered set in the
order topology. If $X$ is compact, then there exist points $c$ and $d$ in $X$
such that $f(c) \leq f(x) \leq f(d)$ for every $x \in X.$

For a proof of this version, see chapter 3 of Munkres' *Topology.*

We'll use it in the following form:

**Theorem:** Let $K$ be a nonempty compact set and $f: K \rightarrow \mathbb{R}$
be continuous. Then $f$ attains both a maximum and a minimum value on $K.$

While we're at it, we might as well just go ahead and prove it, right?

**Proof:** Since the continuous image of a compact set is compact, we know that
$f(K)$ is a compact subset of $\mathbb{R}.$ By the Heine-Borel theorem, this
implies that $f(K)$ is both closed and bounded. Since $f(K)$ is bounded, there
exist real numbers $M$ and $m$ such that $M = \sup f(K)$ and $m = \inf f(K)$.
Furthermore, $f(K)$ is a closed set, hence it contains all its limit points.
Since both $\sup f(K)$ and $\inf f(K)$ are limit points of $f(K),$ we have that
$m \in f(K)$ and $M \in f(K).$ Consequently, $M$ and $m$ are not just abstract
bounds but are actual values attained by the function $f$. Therefore, there
exist points $k_m, k_M \in K$ such that $f(k_{min}) = m$ and $f(k_{max}) = M.$
This completes the proof. $\square$

As you can see, the extreme value theorem isn't particularly exciting, either.
But, at least you don't have to go through 200 pages of a complex analysis
course to get to it.

## My new favorite proof of the Fundamental Theorem of Algebra (finally!)

We're going to use the extreme value theorem as we have proved it --- and not
much more --- in order to prove the fundamental theorem of algebra. Let's go
ahead and dive right in:

**Theorem (Fundamental Theorem of Algebra):** Every non-constant complex
polynomial has a root in $\mathbb{C}.$

**Proof:** Let $p(z) = a_0 + a_1 z + \dots + a_{n-1} z^{n-1} + a_n z^n,$ with
$a_n \neq 0.$ We also know $a_0 \neq 0,$ otherwise this gives us $p(0) = 0.$

As $|z| \to \infty,$ we have that $|p(z)| \to \infty,$ because the $z^n$ term
dominates.[^2] This means we can choose $R$ large enough such that $p(z) \neq 0$
when $|z| >= R.$ Since the disk is a compact subset of $\mathbb{C},$ by the
extreme value theorem, we know $|p(z)|$ also attains a minimum on the disk at
some $z = z_0.$ Since we know $p(z) \neq 0$ on the disk when $|z| = R,$ this
implies that we have $|z_0| < R.$

If $p(z_0) = 0,$ we're done, so let's assume $p(z_0) \neq 0.$ By translating and
scaling $p(z),$ if necessary, we may assume that $z_0 = 0$ and that $p(z_0) =
1.$ Let's call this translated and scaled polynomial $\hat{p}(z),$ and write it
as

$$\hat{p}(z) = 1 + b_k z^k + b_{k+1} z^{k+1} + \dots + b_{n-1} z^{n-1} + b_n
z^n,$$

where $k > 0$ and $b_k$ is the first nonzero coefficient after the constant
term.

This time, we consider what happens when $|z| \to 0.$ In this case, $|\hat{p}
(z)| \to 1$ by continuity, and the $z^k$ term dominates[^3] all the rest
of the terms involving $z$ as we get closer and closer to $0.$

Rewriting $b_k z^k$ in polar form, we see that

$$
\begin{align*}
    b_k z^k & = |b_k| e^{i \alpha} \cdot |z| e^{i k\beta} \\
            &= |b_k||z| e^{i (\alpha + k \beta)} \\
            &= |b_k||z| \cdot (\cos (\alpha + k \beta) + i \sin (\alpha + k
            \beta)),
\end{align*}
$$

which makes it clear we can choose $\beta$ such that $b_k z^k$ is real and
negative.  If we then choose $|z|$ sufficiently small so that the $b_k z^k$ term
dominates in the calculation of $|\hat{p}(z)|$, this then makes $|\hat{p}(z)|$
ever so slightly less than $1.$  This contradicts the fact that we had
constructed $\hat{p}(z)$ such that $|\hat{p}(z)|$ achieved its minimum value of
$1$ at $z = 0,$ thus proving the fundamental theorem of algebra. $\square$

# Why this is my new favorite proof of the FTA

What I like about this proof is that, although it comes out a little bit longer
than the proof using Liouville's theorem, not only do you not need to slog
through a couple chapters of complex analysis to understand this proof, it's
just about self contained as it is.

# *All* the gory details

With that said, there are a *few* things that are missing from this exposition
of the proof, which could be filled in further.

## Implicit notions about complex numbers in the proof

Roughly all you need to understand about the complex plane is that:

* Complex polynomials are continuous everywhere,
* The complex absolute value function is continuous everywhere,
* If $f, g$ are continuous functions, then the composition $f(g(z))$ is
  continuous,
* If $f(z)$ is continuous at $z=z_0$ and $f(z_0)$ is defined, then $\lim_{z \to
  z_0} = f(z_0),$
* For any complex polynomial $P(z),$ we have that $\lim_{|z| \to \infty} |P(z)|
  = \infty,$
* A disk centered at any point $z_0 \in \mathbb{C}$ of radius $R,$ *i.e.* $$D =
  \{z \in \mathbb{C} : |z - z_0| \leq R \}$$ is compact, and
* That we may write any $z \in \mathbb{C}$ in polar form as $z = |z| e^{i
  \theta},$ or, equivalently, $z = |z|(\cos \theta + i \sin \theta),$ for some
  real $\theta,$ which we may restrict to $0 \leq \theta < 2 \pi,$ should we
  wish (a.k.a. Euler's identity).

*However,* I'd argue that all but this last property are not properties of
$\mathbb{C}$ *itself,* rather that they are properties of metric spaces or even
more general topological spaces that also apply to $\mathbb{C}$ as the metric
space $\mathbb{R}^2$ with the Euclidean norm. Moreover, these are fairly
intuitive properties for someone who's gone through a basic, first semester
undergrad calculus course, in the very strong sense that if one were to prove
all of these hold for $\mathbb{C},$ then the proofs would look exactly like the
proofs for $\mathbb{R},$ if we hold in our heads the idea that $|z|$ means "the
distance from $z$ to $0$," in both systems.

## A note on using Euler's identity

The ultimate goal of using the form $z = |z| e^{i \beta}$ in the proof was to
make it easy to get to the equation:

$$b_k z^k = |b_k| |z|^k (\cos (\alpha + k \beta) + i \sin (\alpha + k \beta)),$$
allowing us to choose $\beta$ such that

$$\begin{align*}
    \sin \alpha + k \beta &=& &0, \textrm { and}\\ 
    \cos \alpha + k \beta &=&-&1,
\end{align*}$$

as well as to choose $|z|$ so that $|z|^k$ is sufficiently small.

Alternatively, we could have set $b_k = |b_k| (\cos \theta + i \sin \theta)$ and
made the semi-magical choice of letting $\epsilon > 0$ be arbitrarily small and
letting

$$z = \frac{\epsilon^{1/k}}{|b^k|^{1/k}} \cdot \left(\cos \left[\frac{\theta}{k}\right]  - i \sin \left[\frac{\theta}{k}\right]\right)
                                   \cdot \left(\cos \left[\frac {\pi} {k} \right]  + i \sin \left[\frac{\pi}{k} \right]\right),$$


so that 

$$\begin{align*}
    z^k &= & & \frac {\epsilon} {|b_k|} \cdot (\cos \theta - i \sin \theta) \cdot \left(\cos \pi + i \sin \pi\right) \\
        &= & & \frac {\epsilon} {|b_k|} \cdot (\cos \theta - i \sin \theta) \cdot (-1 + i \cdot 0) \\
        &= &  -&\frac {\epsilon} {|b_k|} \cdot (\cos \theta - i \sin \theta),
\end{align*}$$

by de Moivre's formula.  We then see that 

$$\begin{align*}
    b_k z^k &= |b_k| (\cos \theta + i \sin \theta) \cdot - \frac{\epsilon}
    {|b_k|} (\cos \theta - i \sin \theta) \\
            &= -\epsilon \cdot (\cos \theta   + i \sin \theta) \cdot (\cos \theta - i \sin \theta) \\
            &= -\epsilon \cdot (\cos^2 \theta - i^2 \sin^2 \theta) \\
            &= -\epsilon \cdot (\cos^2 \theta + \sin^2 \theta) \\
            &= - \epsilon,
\end{align*}$$

with a little help from the Pythagorean theorem.  That tells us that for this
particular choice of $z,$ we have that $b_k z^k$ is real, negative, and
arbitrarily small, which is exactly what we need to make the rest of the proof
go through.
This approach has the advantage of avoiding Euler's formula $z = e^{i\theta},$
but with such an arbitrary choice of $z,$ it seems "magical."  Therefore, for
pedagogical and expositional purposes, I think the path I chose to take was the
better one.

## Unproven notions in the proof of the Extreme Value Theorem

I will admit, there are a few background ideas in my proof of the extreme value
theorem, that are not proven here, namely that:

* The continuous image of a compact set is compact,
* The Heine-Borel theorem,
* If $E$ is a set, then $\sup E$ and $\inf E$ are limit points of $E,$ if they
  exist, and
* That a closed set contains all its limit points.

I admit, these are a bit less intuitive for a student who's only gone through a
first semester undergrad calculus course, but not terribly hard to prove in any
respect. What's more, these notions are not hidden by any means; rather, they
are called out fairly explicitly. And, *none* of these are properties that are
*in any way* specific to either $\mathbb{R}, \mathbb{R}^2,$ or $\mathbb{C}.$

## Teaching this proof

I *think* that more or less covers what you'd need to fill in in order to have
an absolutely, 100% complete and rigorous proof of the Fundamental Theorem of
Algebra. In a journal article, for instance, in *The American Mathematical
Monthly,* (a.k.a. *The Monthly*), *The Mathematical Intelligencer,* or some
other expository or educationally focused journal, the proof I gave would
probably be sufficient, even without proving the extreme value theorem in this
setting.

This being my personal blog affords me the luxury of not having to
worry about page limits and such, giving me the ability to add all this
commentary.  Normally, I wouldn't go through all this for a little ~1 page
proof, but I wanted to explain the choices I made in writing the proof itself.
The key point here is that this proof, while not *logically* self-contained[^4]
is *pedagogically* complete in the sense that you can bring it into a Calc 1
class, and have some hope that the students will understand it.  I think that's
pretty cool.

# Historical context (or: what makes this proof truly cool)

As I showed in the previous section, this proof is very self-contained, from a
pedagogical point of view.  Besides that, and the fact that this is probably the
most elementary, self-contained proof of the theorem out there, there's one more
thing that makes this proof interesting: it's actually very similar in structure
to what's regarded as the first serious attempt at a proof of the Fundamental
Theorem of Algebra, by d'Alembert, in 1746.

D'Alembert's proof depended critically on a lemma that stated, but did not prove
rigorously. Although the first rigorous proof was given around 1814[^5] by
Argand, the result is still known as "D'Alembert's Lemma."[^6]

**D'Alembert's Lemma:**  Let $p(z)$ be a non-constant complex polynomial.  If
$p(a) \neq 0,$ then every neighborhood of $a$ contains a point $z$ such that
$|p(z)| < p(a)|.$

And, this is essentially what the second half of the proof I gave argues,
leading to the contradiction that establishes the Fundamental Theorem of
Algebra!

D'Alembert was not only unable to prove his lemma, he didn't have a proper
notion of compactness available to him.  So, he could not have carried through
the argument we have here, using the extreme value theorem and the behavior of
$|p(z)|$ as $|z| \to \infty$ to conclude that there must be some disk of radius
$R$ where $|p(z)|$ attains a minimum.  Lacking said notion of compactness, he
assumed that such a minimum existed.  However, it's easy to see that once you
have proven that $|p(z)|$ attains a minimum, D'Alembert's lemma (which is true,
though not proven by him), then immediately allows you to conclude that said
minimum is $0,$ and that establishes the Fundamental Theorem of Algebra.

In a sense, this means the proof I've given here is the first attempted proof of
the FTA,  but with the gaps filled in.  And, that, I think is very cool.

<hr style="width: 61.8%; color: #404040; height: 1px;
background-color:#404040;"/>


[^1]: That is, again, something that sounds interesting on its face, but turns
out not to be just because it's always going to be the case when you're dealing
with "nice" functions. It turns out that almost all complex-valued functions
are, in a precise sense, *not* nice, but also that there are enough nice
functions that if you squint and restrict the domain you're looking at enough,
you can pretend that nasty function $\mathfrak{F}(z)$ is actually this nice
function $f(z).$ This, however, is a rant for another day.

[^2]: Here, when we say that the $z^n$ term "dominates" in the calculation of 
$\lim_{|z| \to \infty} |p(z)|,$ what we are saying is that there is some real
number $R > 0$ such that if $|z| > R$, then we have 
$$
|z^n| > |a_{n-1} z^{n-1} + a_{n-2} z^{n-2} + \cdots + a_2 z^2 + a_1 z + a_0|,
$$
no matter the choice of $|z|.$  This essentially allows us to think about
$$
|p(z)| = |a_n z^n| + \mathcal{O}(\textrm{don't care}).
$$
In other words, $|p(z)|$ "behaves like" $|a_n z^n|,$ so we can just pretend
we're working with $p(z) = a_n z^n$ directly, and "forget about" most of the
terms.  This, understandably, makes live quite a bit easier when it is possible.

[^3]: Analogously to the previous note, in this situation, as $|z| \to 0$, we 
see that for
$$
\hat{p}(z) = 1 + b_k z^k + b_{k+1} z^{k+1} + \cdots + b_{n-1} z^{n-1} + b_n
z^n
$$
when $|z|$ is sufficiently small, we have 
$$
|z^k| >|b_{k+1} z^{k+1} + \cdots + b_{n-1} z^{n-1} + b_n z^n|,
$$
allowing us to think about $|\hat{p}(z)| = |1 + b_k z^k| +
\mathcal{O}(\textrm {don't care}),$ and pretend we're working  with
$\hat{p}(z) = 1 + b_k z^k$ directly.

[^4]: Not that I've ever seen a fully, logically self-contained proof that's
    intended to be *read* rather than *run* (*i.e.* a proof that isn't a program
    written for a proof checker).

[^5]: Sources vary on this.  Argand apparently published a proof sketch around
    1806 that gave the outline of the full proof he would publish later.  I've
    seen dates ranging from 1813-1815 for the exact date of publication.

[^6]: Although, technically speaking, it should really be called "*Not*
    D'Alembert's Lemma." But, that's just nitpicking at this point.
