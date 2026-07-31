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
MemDorge seperates raw information, interpatetion,evaluation and persistent knowledge imto distinct cognitive layers.
The cognitşve pipeline follows:
Observation → Claim → Evidance → Belief → Memory
Each layer represents a diffrent stage in Noema's cognitive process
## 2.1 Observation
An observation is the raw input received froma a conversation or external source.
Observations represent  what was observed , not what is true
An Observation contain the original information without interpretation, assumptions, or evaluation.
Example :

Input :
' The user said ı am learning STM32.'

Observation:
'User mentioned STM32.'
Observation properties:
-Immutable
-Timepstamped
-Context-dependent
-Does not contain interpretation
- Is not a memory

## 2.2 Claim



A claim is an interpreted statement generated from one or more observations.
Claims represent Noema's current interpretation of available observations. They are not considered permanent facts and must not directly become memories.
A claim reflects the currentunderstanding of the system at a spesific point in the time. It can be strengthened, weakened,revised,or rejected as new evidance becomes available.
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
 ## 2.3 Evidance
 Evidance is information that supports, weakens or contradictsa claim.
 Evidance does not represent raw input. Instead, it represents the relationship between available information and a  spesific claim.
 Evidance allows Noema to evaluate the reliability, evoluation,and consistancy of claims over time.
 
 Example:

 Observation:
 
' The user said : I am learning STM32.'
 
 Claim at this point:
 'This user is interested in embedded systems.'  
 
 Supporting Evidance:
 'This user is has ciscussed STM32 ,ESP32,Arduino,and embadded projects multiple times.' 

Contradicting Evidance:
'This user states that embadded systems are no longer a field of interest.'

Evidance Properties:

-Assosiated with one or more claims
- Can support or contradigt a claim
- Has temporal context
- Has a source 
- Influence belief revision 

## 2.4 Belief
A belief is Noema's current confidence state toward a spesific point in the time.
Beliefs are dynamic cognitive states that evolves ad new evidance becomes available.
A belief does not representa absolute truth. It represents the current evolution of a claim based on available evidance, hiistorical context,and consistency.

Example:
 
Claim at this point: 
'The user is interested in embedded systems.'

Evidance:
' The user has repetedly discussed STM32, ESP32, and embedded projects.'

Belief:
' High likelyhood that the user has a sustained interest in embedded systems.

Evidance Properties:
- Associated with one or more claims
- Can support or contradict a claim
- Has temporal context
- Has a source
- Influence belief revision

## 2.5 Memory
Memory is the persistent representation of the information the Noema chooses to preserve after cognitive evaluation
Memory is not a direct stogare of observations. It is the result of a selection process based on relevance ,consistency,and long-term value
Noema does not remember everything it observes.It preserves information that contributes to a more accurate and useful understanding of the user

Example:

Observation:
'The user mentioned drinking coffee today.'

Belief:
' Temporary daily activity.'

Memory decision:
Not preserved.
---
Observation:
'The user is studying electrical engineering.'

Claim at this point:
'The user has a long-term interest in engineering.'

Evidance:
'Repeated discussions about engineering topics,projects, and career goals.'

Belief:
'High confidence.'

Memory decision:
Preserved as long-term user context.

Memory properties:

- Derived from evaluated beliefs.
- Long-term oriented
- Selectively preserved
- Can be updated or removed
- Represents meaningful context

## 3. Cognitive Architecture
Noema is designed a cognitive middleware layer independent from the underlying language model
The system does not generate conservations or replace the reasoning capabilities of an LLM. Instead , it provides a persistent cognitive layer that observes, interprets, evaluates, and preserves information across interactions.
The architecture consists of several independent components:

Observation Layer
    ↓
Claim Layer
    ↓
Evidance Layer
    ↓
Belief Revision Engine
    ↓    
Memory Layer

## 3.1 Observation Layer

The Observation Layer is responsible for capturing raw information from externl sources.
Its primary purpose is to collect information without interpretation or assumption.
The Observation Layer does not decide meaning. It only recordswhat was observed and provides structured input for higher cognitive layers.

Responsibilities:
- Capture raw inputs
- Attach timestamps and context
- Preserves original information
- Provide data for claim generation

The Observation Layer must remain independent from belief formation.

 ### 3.2 Claim Layer
 The Claim Layer is responsible for generating interpretend statementsform observations.
 A claim is not a fact. It represents Noema's current understanding of available information at a spesific point in time.
 The claim Layer transforms raw observations into meaningful hypotheses while preserving uncertainty.
 The Claim Layer  does not create permanent memory. It ınterpretable representations that can later be evaluated by the Evidance and Belief layers.

 Responsibilities:
 - Analyze observations
 - Generate candidate interpretations
 - Maintain context between observations
 - Link claims to their originating observations
 - Preserve uncertainty during interprations
  
   The Claim Layer must avoid premature cocnlusions and should not convert a single observation into a permanent user attribute.

   Example:

   Observation:
   'The user mentioned Python several times.'

   Claim at this point:
   ' The user may have an interest in programming.'
   
   The claim remains open to future evidence and revision

   ###  3.3 Evidance Layer
   The Evidance Layer is responible for managing the relationship between information sources and claims.
   Evidence does not represent raw observations. It represents how available information affects the evalution of a spesific claims.
   The Evidance Layer allows Noema to track supporting information, contradiccting information, and changes in understanding over time.

   Resposibilities:
   - Associate evidence with claims
   - Track supporting and contradicting evidence
   - Maintain temporal context
   - Preserve evidance sources
   - Provide information for belief revision

   Evidance types:

   Supporting Evidance:
   Information thar increases confidance in a claim

   Contradicting Evidence:
   Information that decreases confidance in a claim.

   Example:
   
   Claim at this point:
   'The user is interested in programming.'

   Supporting Evidence:
   'The user has repeatedly discussed Python projects and software development.'

   Contradicting Evidence:
   'The user states that programming is no longer a field of interest'

   The Evidence Layer does not determine final belief values. It provides structured information for the Belief Revision Engine.

   ### 3.4 Belief Revision Engine
   The  Belief Revision Engine is responsible for maintaining the current belief state of Noema.
   Its purpose is to continiously claims as new evidance becomes available.
   Rather than treating beliefs as fixed values, the engine updates them over time according to accumulated evidance, contradictions, temporal context,and consistency.

   Responsibilities:
   - Update belief states
   - Evaluate supporting and contradicting evidence
   - Resolve conflicting information
   - Consider temporal relevance
   - Maintain belief consistency

   The Belief Revision Engine does not generate claims or store memories.
   Instead, it determines the current cognitive state of existing claims.

   Example:
    
    Claim:
    'The user is interested in programming.'

    Supporting Evidence:
    -The user discusses Python regularly.
    - The user contributes to software projects.

    Contradicting Evidence:
    - The user states that programming is no longer a career goal.

    Belief Outcome:
    The belief is updated to reflec the current balance of available evidence rather than permanently accepting or rejecting the claim

     3.5 Memory Layer
    The Memory Layer is responsible for preserving information that has passed cognitive evaluation.
    Rather than storing every observation or claim , the Memory Layer selectively retains information that contributes a stable and meaningful understanding of the user.
    Memory creation is based on the current belief state, accumulated evidence,and long-term relevance.
    
    Responsibilities:
    - Preserve meaningful information
    - Create persistent memory records
    - Update existing memories
    - Remove or archive obsolete memories
    - Provide long-term context for future reasoning

    The Memory Layer does not generate interpretations or evaluate evidance.It only manages information that has already been cognitively validated.
    
    Memory decisions are reversible. As beliefs evolve, memories may be updated, replaced, or removed.

    ## 4. Cognitive Pipeline

    The Cognitive Pipeline describes how information flows through Noema.
    Each Layer has a single responsibility and operates independently from the others.Information progresses through susscesive stages of interpretation, evaluation, and preservation.

    Pipeline
    User Input
       ↓
    Observation Layer
       ↓    
    Claim Layer
       ↓
    Evidence Layer
       ↓
    Belief Revision Engine
       ↓
    Memory Layer
       ↓
    Persistent Memory

    Pipeline Stages
    1- Observation
    Capture raw information without interpretation.
    2- Claim
    Generate one or more candidate interpretations.
    3- Evidence
    Associate supporting and contradicting informatşon with each claim.
    4- Belief Revision
    Update the current belief state according to available evidance
    5- Memory
    Preserve cognitively validated information for long-term use.

    The cognitive Pipeline is strictly sequential.
    Each layer is responsible only for its own task and must not bypass or replace the responsibilities of another layer.
    This seperation ensures transparency, explainability, and modularity throughout the cognitive system.            

     ## 5. Cognitive Principles
     The following principles define the fundamental behavior of Noema.
     These principles are implementation-independent and must remain regardless of future architecturaş changes.
     ### Principle 1 - Observations Are Not Truth
      Observations represent what has been received, not what is objectively true.
      Noema must preserve observations without assuming their correctness.
      ---
     ### Principle 2 - Claims Are Interpretations
     Claims are cognitive interpretations derived from observations.
     A claim must never be treated as a permanent fact without continious evaluation.
      ---
      ### Principle 3 - Beliefs Are Revisable
     Every belief is subject to revision.
     New evidance may strengthen, weaken, or invalidatean existing belief
     ---
      ### Principle 4 - Memory Is Selective
     Noema does not preserve every piece of information.
     Only cognitively validated information with long-term relevance  should become memory.
     ---
      ### Principle 5 - Contradictions Are Information
     Contradictions are not errors.
     Conflicting information is part of human cognition and must contribute to belief revision rather tahn immediate replacement.
      
      ## 6. Future Directions
      Noema's architecture is designed to support future extansion while preserving the core cognitive model.
      Future development may expand the system beyond its initial capabilities while maintaining the seperation between observation, interpretations, evaluation, and memory

       ### 6.1 Explainable Cognition
       Future versions may introduce mechanisms that allow Noema to explain the reasoning behind cognitive decisions.

       Potential Capabilities:
       - Explain why a memory was created
       - Trace beliefs back to supporting evidance
       - Ispect belief changes over time
       - Provide cognitive decision history

       ---
       
       ### 6.2 Active Cognitive Interferance
       Future versions may allow direct interaction with Noema as a cognitive engine.

       Possible Capabilities:

       - Cognitive analysis commands
       - Belief inspection
       - Memory management operations
       - System-level reasoning requests

       ---

        ###  6.3 Advanced Belief Modeling
        Future research may explore more sophisticated belief models.

        Possible Improvement:
         
       - Confidence evolution over time
       - Belief decay mechanisms
       - Probabilistic belief representation
       - Complex contradiction handling

       ---

        ### 6.4 Cognitive Graph Structures
        Future versions may represent cognitive realtionships as interconnected graphs.

        Potential structures:

        - Claim graphs 
        - Evidence networks
        - Belief Relationships
        - Semantic memory connections

        ---

        ### 6.5  Multi-Agent Cognitive Systems
        Noema's architecture may be extanded to support multiple cognitive agents sharing or comparing knowledge structures.

        Possible applications:

        - Collabritive AI systems.
        - Distributed memory architectures
        - Collective reasoning systems

        ### 7. Data Model
        The Data Model defines the interval cognitive objects used by Noema
        Each object represents a spesific stage of the cognitive process and has a clearly defined responsibility.
        The data model is independent from any storage engine or database implementation.
        Whether the system uses SQL, NoSQL, Graph databases, or custom storage, the cognitive model remains unchanged. 

        ### 7.1 Observation 
        An Observation represents a raw piece of information received by Noema.
        It contains the original input without interpretation or evaluation.

        Properties:
        - Observation ID
        - Source
        - Timestamp
        - Raw Content
        - Context Metadata
         
         Observations are imutable once created.

         ### 7.2 Claim 
         A claim represents an interpreted understanding derived from one or more observations.
         Claims are Dynamic objects whose cognitive state may evolve over time.

        Properties:
        - Claim ID
        - Related Observation IDs
        - Claim Content
        - Creation Timestamps
        - Current Status
         Claims may be updated as new evidance  becomes available

        ### 7.3 Evidence
        Evidence represents the relationships between observations and claims.
        Evidancee does not store knowledge.
        Instead , it records how available information influences the evoluation of a claim.
        
        Properties:
        - Evidence ID
        - Associated Claim
        - Source Observation
        - Evidence Type
        - Timestamps

        ### 7.4 Belief
        A Belief represents Noema's current cognitive confidence in a claim.
        Beliefs are independent cognitive objects associated with claims.
        Seperating beliefs from claims allows the system to maintain evolving cognitive states without modifying the original interpretations.

       Properties:
       - Belief ID
       - Associated Claim ID
       - Current State
       - Creation Timepstamp
       - Last Updated
       - Revision Count

       Beliefs are continiously updated as a new evidance becomes available

        ### 7.5 Memory
        A Memory represents cognitively preserved information derived from evaluated beliefs.
        Memories are not maintains a connection to its underlying cognitive history while serving as long-term contextfor future ınteractions.

         Properties:
       - Memory ID
       - Associated Belief ID
       - Memory Content
       - Creation Timestamp
       - Last Updated
       - Status

       Memories may be updated,archived, or removed as beliefs evolve.

       ### 8. Implementation Principles 
       The following principles defines the engineering constraints for implementing Noema
       These principles ensure that diffrent implementations remain consistent with the cpgnitive model.
      
       ### 8.1 Modularity
       Each cognitive component should be implemented as an independent module with clearly defined responsibilities.
      
       ---
       ### 8.2 Deterministic Processing
       Given the same observatşons and the same cognitive state, Noema should produve the same cognitive outcome.
       
       ---
       ### 8.3 Storage Independence
       The cognitive model must remain independent from any database or storage technology.
       Storage is an implementation detail, not a cognitive component.
      
       ---
       ### 8.4 Extensibility
       The architecture should allow future cognitive capabilities to be introduced without requiring fundamental changes to the existing model.

      ---
      ### 8.5 Replaceability
      individual cognitive components should be replaceable without affecting the overall architecture, provided they preserve the same behavioral spesification

      ---
      ### 8.6 Traceability
      Every cognitive object should maintain references to objects from which it originated.
      Observation → Claim → Evidence → Belief → Memory
      The cognitive chain should remain traversable throuhout the system.
         
     ### 8.7 Implementation Before Optimization
     Correct cognitive behavior takes priority over performance optimizations.
     The reference implementation should prioritize correctness, clarity, and maintainability over execution speed.
