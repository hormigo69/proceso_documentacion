De moento voy a recopilar información para oreedenar después:


Alguien utiliza la pregunta 'scrutinize <SOMETHING>', pe: scrutinize this plan?
Junta a un personality como este:
Be adversarial and critical — no softening, no compliments.
Identify flaws, contradictions, weak spots, and assumptions.
Look for risks and pain-points — technical, conceptual, organizational.
Challenge feasibility — scalability, maintainability, real-world edge cases.
Point out what’s missing — gaps in logic, overlooked constraints, hidden dependencies.
Play devil’s advocate — think like a hostile reviewer, competitor, or strict auditor.
Prioritize weaknesses over strengths — strengths only if relevant to expose trade-offs.

Entonces ya no es tan 'supportive' 🙂
Por lo general los modelos mejores en ingeniería no son tan supportive

Solo los modelos pequeños y baratos más generalistas

- Entiendo que esto está bien para ponerlo en las instrucciones de chatGPT normal, no?

[13:59, 29/8/2025] +33 6 52 67 27 57: preparas mails en cursor? me perdi ahi
[14:17, 29/8/2025] +34 618 73 69 46: Realmente puedes pedir cualquier cosa 🙂
[14:18, 29/8/2025] +34 618 73 69 46: Yo he estado usando GHC para demostrar papers
[14:19, 29/8/2025] +34 618 73 69 46: Una idea es usar markitdown y tenerlo en el repo local para usar con contenido directamente

[13:43, 29/8/2025] +34 600 66 03 61: Los uso para claude code.
[13:44, 29/8/2025] +34 600 66 03 61: Pero, sí para gpt tb.

[14:19, 29/8/2025] Juanjo do Olmo (IA): Claro
[14:19, 29/8/2025] Juanjo do Olmo (IA): Documentos, papers, mails, posts, noticias, yo hago todo en Cursor desde la Beta casi
[14:27, 29/8/2025] +34 670 65 74 52: Pero tienes como un repositorio de textos a modo de carpetas o como lo organizas
[14:28, 29/8/2025] Juanjo do Olmo (IA): Claro
[14:29, 29/8/2025] Juanjo do Olmo (IA): Cada proyecto tengo un repositorio con todos los docs en .md
Plantillas e instrucciones
Y con eso hago virguerías
Mucho mejor q chatGPT vaya
Es un second brain



[14:31, 29/8/2025] +34 670 65 74 52: Entonces por ejemplo vas a redactar un email de curro y te vas al proyecto de emails profesionales, y ahí tienes plantillas y un read me con instrucciones de redacción y en cursor le dices que te consulte todo eso para escribir lo que quieres en el documento.md
[14:31, 29/8/2025] +34 670 65 74 52: Es así?
[14:32, 29/8/2025] +33 6 52 67 27 57: y con mails del pasado que quieras que use como referencia y tal. 
No se a que esperamos para wrappearlo para normies esto
[14:32, 29/8/2025] +33 6 52 67 27 57: o sea yo no lo hago asi pero ha sido leer la linea y ya se que acabo de upgradear mi vida

A esto se le suma el post de ANdrej Karpathy :
Post: https://x.com/karpathy/status/1961128638725923119?s=46&t=izXsMAEznST3ivyoGCfhAg

@karpathy
Transforming human knowledge, sensors and actuators from human-first and human-legible to LLM-first and LLM-legible is a beautiful space with so much potential and so much can be done...

One example I'm obsessed with recently - for every textbook pdf/epub, there is a perfect "LLMification" of it intended not for human but for an LLM (though it is a non-trivial transformation that would need human in the loop involvement).

- All of the exposition is extracted into a markdown document, including all latex, styling (bold/italic), tables, lists, etc. All of the figures are extracted as images.
- All worked problems get extracted into SFT examples. Any referenced made to previous figures/tables/etc. are parsed and included.
- All practice problems are extracted into environment examples for RL. The correct answers are located in the answer key and attached. Any additional information is added as "answer key" for a potential LLM judge.
- Synthetic data expansion. For every specific problem, you can create an infinite problem generator, which emits problems of that type. For example, if a problem is "What is the angle between the hour and minute hands at 9am?" , you can imagine generalizing that to any arbitrary time and calculating answers using Python code, and possibly generating synthetic variations of the prompt text.
- All of the data above could be nicely indexed and embedded into a RAG database for later reference, or maybe MCP servers that make it available.

Then just as a (human) student could take a high school physics course, an LLM could take it in the exact same way. This would be a significantly richer source of legible, workable information for an LLM than just something like pdf-to-text (current prevailing practice), which simply asks the LLM to predict the textbook content top to bottom token by token (umm - lame).

As just a quick and crappy example of synthetic variations of the above example, GPT-5 gave me this problem generator (see image), which can now generalize that problem template to many variations:

- When the time is 11:07 a.m., what is the degree measure of the angle between the hands? (Answer: 68)
- Determine the angle in degrees between the clock’s hands at 4:14 a.m.. (Answer: 43)
- What angle do the clock hands form when the time reads 11:47 a.m.? (Answer: 71)
- At 7:02 a.m., what angle separates the hour hand and the minute hand? (Answer: 161)
- At 4:14 a.m., calculate the angle made between the two hands. (Answer: 43)
- What angle is formed by the hands of a clock at 4:45 p.m.? (Answer: 127)
- What is the angle between the hour and minute hands at 8:37 p.m.? (Answer: 36)
(infinite practice problems can be created...)

y:
Post: https://x.com/karpathy/status/1960803117689397543?s=46

@karpathy
In era of pretraining, what mattered was internet text. You'd primarily want a large, diverse, high quality collection of internet documents to learn from.

In era of supervised finetuning, it was conversations. Contract workers are hired to create answers for questions, a bit like what you'd see on Stack Overflow / Quora, or etc., but geared towards LLM use cases.

Neither of the two above are going away (imo), but in this era of reinforcement learning, it is now environments. Unlike the above, they give the LLM an opportunity to actually interact - take actions, see outcomes, etc. This means you can hope to do a lot better than statistical expert imitation. And they can be used both for model training and evaluation. But just like before, the core problem now is needing a large, diverse, high quality set of environments, as exercises for the LLM to practice against.

In some ways, I'm reminded of OpenAI's very first project (gym), which was exactly a framework hoping to build a large collection of environments in the same schema, but this was way before LLMs. So the environments were simple academic control tasks of the time, like cartpole, ATARI, etc. The 
@PrimeIntellect
 environments hub (and the `verifiers` repo on GitHub) builds the modernized version specifically targeting LLMs, and it's a great effort/idea. I pitched that someone build something like it earlier this year:
https://x.com/karpathy/status/1884676486713737258
Environments have the property that once the skeleton of the framework is in place, in principle the community / industry can parallelize across many different domains, which is exciting.

Final thought - personally and long-term, I am bullish on environments and agentic interactions but I am bearish on reinforcement learning specifically. I think that reward functions are super sus, and I think humans don't use RL to learn (maybe they do for some motor tasks etc, but not intellectual problem solving tasks). Humans use different learning paradigms that are significantly more powerful and sample efficient and that haven't been properly invented and scaled yet, though early sketches and ideas exist (as just one example, the idea of "system prompt learning", moving the update to tokens/contexts not weights and optionally distilling to weights as a separate process a bit like sleep does).

Volvemos al hilo:
[14:50, 29/8/2025] Rafael Benzal AI (Juanjo do Olmo): Por eso pregunté también el otro día el tema de cómo estaban los RAG como servicio, porque es que actualmente para proyectos propios usar Cursor me es lo más cómodo... Porque ya lo tengo xd
[14:50, 29/8/2025] Juanjo do Olmo (IA): Lo de Cursor?
[14:50, 29/8/2025] Juanjo do Olmo (IA): Si, yo igual
[14:50, 29/8/2025] Juanjo do Olmo (IA): El rag nativo de cursor y buena higiene de repos pa cada proyecto y fuera

[14:51, 29/8/2025] Rafael Benzal AI (Juanjo do Olmo): Claro, es que si él ya te monta el índice en el mismo sitio donde tienes la documentación... No me tengo que preocupar de que si actualizo los archivos, puedo usar cualquier modelo para Chat with codebase
[14:51, 29/8/2025] Rafael Benzal AI (Juanjo do Olmo): Me lo tienen que poner muy fino en otro sitio para que me plantee cambiarme en local, pero claro si lo que quiero es apificarlo
[14:52, 29/8/2025] Rafael Benzal AI (Juanjo do Olmo): Porque quiero sacar ese chat por otro lado

[14:59, 29/8/2025] +33 6 52 67 27 57: En plan para normies. Tienes tu proyecto "salud" ahi se acumulan todos los datos objetivos, y se reusan para cualquier pregunta que le hagas por ejemplo

O emails, tienes una carpeta con ejemplos de emails tuyos, y otro con reglas de estilo, y cunado haces click ne nuevo, te va a autocompletando
Otro para guiones de youtube, lo mismo, ejemplos y reglas y te hace lo que le pidas pero full contextualizado etc
[15:03, 29/8/2025] Juanjo do Olmo (IA): Exacto

A ver yo lo veo asi:
1) Editor de texto con buena UX
2) Proyectos y subproyectos que aplican reglas. Cada uno se configura con reglas y con examples
3) Autocompletado y agente
4) El agente es smart y te va aniadiendo cosas a la memoria y cambiandola y puedes hacer push o no de los cambios
5) Lo empiezo con varias templates, email, salud, personal CRM y un ejemplo de proyecto del curro


