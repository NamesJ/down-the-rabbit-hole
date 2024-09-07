# Down the Rabbit Hole
## The purpose of this project (?)
This project simultaneously goes against the very goals of software development while at the same time is perfectly aligned with it's ideals -- because the "solution" in this case is just something I find interesting.

I dedicate this project to those of us that find some joy and wonder in creating software.

And so, down.. down.... down...... into the rabbit hole we go.

Down we go, because we can.

Down we go, because it's a little funny.

Is it funny enough to justify all of the work required to build it? **Ab-so-lute-ly not**.

But, that's funny too, so down we go!

## Okay, okay, so what actually is this "project" then?
I like to call it a `Rube Goldberg Virtual Machine`. But essentially, when a program is executed it will output another program, which itself will output yet another program, which will output yet still another program, and so on. This process continues until one of these happens:
1. You get bored
2. The universe ends. How does it end? I'm actually not sure. I think some people are working on it, though. So I'll update this README.md once they've figured it out
3. The currently running program creates the next program which happens to contain a critical bug. Because each program relies on all of the previous ones working (nearly) perfectly, as the number of programs increases, the likelihood of a crash approaches 100%.
4. I try to `git push` but die instead.

## You said "Rube Goldberg Virtual Machine", so what does it accomplish?
The *last program* to be executed will check this repo for updates. If there are any, it'll download them. Yep, that means it has auto-updates. So no need to incessantly check if a new version is out.

## Will it be interactive?
Yes! I definitely intend to have opportunities for a human-in-the-loop.

## I'm ready to go down the rabbit hole
Lovely to meet you then! You've got gumption! You've got grace! You've got free time!

Naturally, a project like this is going to potentially have a good deal of setup. The hope is to keep it as minimal and automated as possible, but no guarantees.

Right now, the first big red button you press to get this machine clacking and spinning is:
```
git clone [repo_url_here]

python3 down_the_rabbit_hole.py
```