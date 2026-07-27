# MemForge Cognitive Spesification v0.1
## 1. INTRODUCTION
MemForge is a cognitive middleware designed to enable AI systems to buıld evidance-driven long-term memory.
Unlike traditional memory systems, MemForge does not directly transform conversations into memory
Human communication is uncertain. Users may provide incomplete information , change their opinion, misunderstand themselves,or express temporary states. Therefore, individual messages should not be treated as permanent facts.
MemForge  introduces a cognitive layer between conversation and memory.
This layer, called Noema ,continiously evaluates observations,accumalates evidance, revises beliefs, and publishes persistent memories only when sufficient confidence is achieved.
The fundamental principle of MemForge is
> Memory is persistent. Belief is dynamic
Memory represents a stable projection of a continiously evolving belief system
## 2. Core Consepts
A claim is an interpreted statement generated from one of more observations.
Claims represent possible meanings redived from observedinformation.They are not considered facts and must not directly become memories.
A Claim requires supporting evidance before irt can influence the belief system.
Example:
Observation :
' The user said : I am learning STM32.'
 
 Claim at this point:
 'This user is interested in embedded systems.'  
 This claim represents Noema's current interpretation of available observations. İt is not a permanent truth and may be revised when additional evidance is collected.

Claim Properties:
 - Derived from observations
 -Represents current interpretations
 -Not guaranteed to be permanently true
 - Requires evidance evaluation
 -Can evolve over time
 