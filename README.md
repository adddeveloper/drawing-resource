# Drawing Resource

The [json file](https://raw.githubusercontent.com/adddeveloper/drawing-resource/main/index.json) gives us an array that has descriptions of the drawings.

For example:
```
{
  "name": "How to draw a Patterns?",
  "description": ["By combining various lines, shapes, and colors that repeat, you will end up with a beautiful pattern.","patterns"],
  "src": "drawing-resource.netlify.app/images/pattern",
  "final": "image_40.jpg",
  "order": ["image_1.jpg", "image_10.jpg", "..."]
}
```
The "name" is the heading. The "description" has 2 elements, the first being a description, and the second being what we are drawing.
The "src" is where we can find the images. The "final" is the final phase of the drawing. The "order" is the order in which we go through the images to see how we come to the "final".

The python file in the directory of this repo is made by chat gpt. 

---
Please contact if you see any problems or have something to say:
[contact](https://adnans.website)
