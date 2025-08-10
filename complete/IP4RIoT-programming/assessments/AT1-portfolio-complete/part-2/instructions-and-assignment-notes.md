## Instructions
*Assignment due 23/5/2025*  
**Completed 22/5/2025**   
Instructions from blackboard for quick reference:
___

[Blackboard Assessment Link](https://blackboard.northmetrotafe.wa.edu.au/webapps/assignment/uploadAssignment?content_id=_3663737_1&course_id=_35877_1&group_id=&mode=view)

![instruction](./resources/instructions.png)

* [C-RIOT-AT2-Part2.docx](./resources/C-RIOT-AT2-Part2.docx)  
* [Github Link](https://github.com/NM-TAFE/civ-ipriot-smiley)

### Assignment Notes:
* Have forked and branched repo as instructed
* Fork kept at [Serphania](https://github.com/Seraphania/civ-ipriot-smiley) 
* ***Remember to work on the [por2](https://github.com/Seraphania/civ-ipriot-smiley/tree/por2) branch!*** - Branch merged with main after completion.
* [Checklist](GPT-checklist.md) I had GPT make for me so I could get going.
* [.zip of completed assignment](./resources/civ-ipriot-smiley-main.zip)  


### Stretch Goal:
Reimagine the relationship between Smiley and Happy. How can we maintain reusability while _avoiding_ inheritance?  
**Clues**  
- "Happy `has a` Smiley?" doesn't sound right, does it?
- "Smiley `has a` Happy?" sounds even worse!
- What about a Smiley is composed of an Expression?
- What kind of class would Expression be?

**Learn more**
When we do use inheritance, we tend to favour inheriting from abstractions, not concrete classes. For example, it is pretty helpful to standardise everything that an "Expression" can do so that we can (polymorphically) handle expressions, so it makes sense for Happy, Sad, Etc, to inherit from Expression(ABC) and for Smiley to be composed of an expression (which we can pass at instantiation time).

[composition > inheritance](https://www.youtube.com/watch?v=hxGOiiR9ZKg)