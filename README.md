## Inspiration
Inspired by the essence of a company like **Mango**, with _four decades of history and a leadership position in European fashion_, we have endeavored to undertake a project that integrates the latest technological advancements in artificial intelligence to address one of the major challenges in the fashion world: the creation of innovative new outfits capable of standing out in a competitive market.

## What it does
A collection of various artificial intelligence methods has been crafted to tackle this challenge. The main idea of the project is to create new outfits using selected items from Mango's online store or from photos of personal clothing that individuals wish to combine with products from Mango's store.
An interface has been designed in the form of a web page so that users can test the functionality of our project. Users can upload their clothing items or select them directly from Mango's store and receive product recommendations from Mango that can complement their outfit.

## How we built it
In technical terms, the first layer of the model is capable of detecting clothing features such as the type of garment, color, or fabric in the images under consideration. From the extracted features, a numerical code or embeddings is generated through the application of transformers (deep learning models for natural language processing). These numerical codes or *embeddings* are represented in a latent space, in which a *local search* is conducted (including _hill climbing_ techniques). The local search involves making modifications to solution states (outfits considered correct), where new outfit configurations are tested, and they are accepted based on a heuristic. In our case, we have chosen to use a weighting scheme between the average probabilities of different types of features (color, fabric, etc.) appearing in an outfit, along with the Euclidean distance between the embeddings corresponding to each clothing item.
The image detection has been achieved through the implementation of a *convolutional neural network* that classifies images based on the color code and fabric code used by Mango. Additionally, the _YOLO_ model has been used to detect the specific type of clothing item. For the generation of embeddings, the transformer provided by _Fashion Clip_ was employed, and a custom code was created for the Hill Climbing method and local search. For the development of the app web, Streamlit and  CSS.

## Challenges we ran into
The challenges being addressed include the creation of new outfits that are competitive in the market. Additionally, it aims to solve the issue of user indecision when it comes to combining clothing items.

## Accomplishments that we're proud of
We are proud of having navigated the cutting-edge realm of technologies, specifically the transformers models. Also, of our ability to handle pressure efficiently and manage timelines effectively has been a standout aspect of our collaboration. Moreover, we firmly believe that the innovative idea underlying our project is not only groundbreaking but also holds significant utility in addressing contemporary societal needs.

## What we learned
We have delved into advanced topics such as transformer-based AI models, explored more straightforward AI algorithms like local search, and honed our skills in manipulating and utilizing embeddings. Beyond technical aspects, we've also seen significant improvements in our soft skills, particularly in areas like teamwork, collaboration, and thriving under pressure. It's been a comprehensive journey of learning and growth.

## What's next for "MANGO" -  H&B - Fashion Copilot
Despite presenting a tangible project, there is a significant room for advancement. With access to a larger dataset, the chosen heuristic could be optimized by improving the probabilistic weights used to combine different features. Additionally, better training of the model could enhance prediction accuracy. Finally, with access to data associated with temporal dates, it would be possible to evaluate a periodic pattern in fashion styles and introduce coefficients that incorporate a temporal dependency into the model.
