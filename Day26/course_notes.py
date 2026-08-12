"""
Day 25 · Shared knowledge base — YOUR OWN COURSE NOTES
Today's documents are the notes from this very course. We'll build a system
that can answer questions about them.
    from course_notes import NOTES
    NOTES is a list of (title, text) pairs.
Needs:  nothing (pure Python)
"""

NOTES = [
    ("Train/test split",
     "We always hold back part of the data as a test set. The model never sees it during "
     "training, so its score on the test set is an honest estimate of how it will do on new "
     "data. A typical split is 75 percent for training and 25 percent for testing. Always pass a "
     "fixed random state so the same rows land in the same side every run, otherwise your score "
     "wobbles for reasons that have nothing to do with the model. For classification, stratify the "
     "split so each side keeps the same class balance as the original data, which matters a lot "
     "when one class is rare. The golden rule is that you look at the test set once, at the very "
     "end. If you tune settings against it, its score stops being honest, because you have quietly "
     "started fitting to it. That is why serious projects use three slices: train to fit, "
     "validation to tune, and test to report. With time-ordered data, split by date rather than at "
     "random, so you always train on the past and test on the future."),

    ("Overfitting",
     "Overfitting is when a model memorises the training rows instead of learning the pattern. "
     "The sign is a large gap between train accuracy and test accuracy, for example train 1.000 "
     "but test 0.771. A model that is perfect on training data but weak on new data has memorised, "
     "not learned. It happens when the model has more capacity than the data can support: a tree "
     "grown to full depth, a network with too many weights, or simply too few rows for the number "
     "of columns. The opposite failure is underfitting, where the model is too simple and scores "
     "poorly on both train and test, and the two are told apart by that gap. The usual cures are "
     "more data, a simpler model, limits such as maximum depth or minimum samples per leaf, "
     "regularisation, averaging many models as a forest does, and early stopping for networks. "
     "Check the gap on every model you fit, not just the final one."),

    ("Cross-validation",
     "Cross-validation splits the data into k folds, trains on k minus one of them and tests on "
     "the held-out fold, then rotates and averages. It gives a steadier, more honest score than a "
     "single split, reported as mean plus or minus standard deviation. Five or ten folds is the "
     "normal choice, and for classification you want the stratified version so every fold keeps "
     "the class balance. The standard deviation is as informative as the mean: a wide spread means "
     "your estimate depends heavily on which rows you happened to hold out, which is a warning that "
     "the dataset is small or uneven. The cost is that you train k models instead of one. Use it "
     "for comparing models and choosing settings, and still keep a separate final test set, "
     "because choosing the winner out of many candidates is itself a form of fitting."),

    ("Data leakage",
     "Leakage happens when information from the test set sneaks into training, for example fitting "
     "a scaler on all the data before splitting. The fix is to put every transformer inside a "
     "Pipeline so it is fitted on the training fold only. Leakage comes in other flavours too. "
     "Target leakage is a column that would not exist at prediction time, such as a discharge date "
     "when predicting admission, or an outcome flag someone filled in later. Duplicate or "
     "near-duplicate rows landing on both sides of the split let the model recognise rows it has "
     "already seen. Time leakage is training on the future to predict the past. The symptom is "
     "always the same and always seductive: a score that looks too good, holds up in your notebook, "
     "and collapses in production. If a result surprises you by being excellent, suspect leakage "
     "before you celebrate."),

    ("Decision tree",
     "A decision tree asks a series of yes or no questions about one feature at a time, such as "
     "is worst radius less than seventeen. It chooses each question by measuring Gini impurity and "
     "keeping the split that makes the child groups purest. Its strength is that you can read it. "
     "The points where it asks a question are internal nodes, the end points that give an answer "
     "are leaves, and the longest path from top to bottom is the depth. It is built greedily: at "
     "each node it takes the best split available right now, without checking whether a worse split "
     "now would allow a better one later. Left alone it will grow until every leaf is pure, which "
     "is memorisation, so it is controlled with maximum depth, minimum samples per leaf, or minimum "
     "impurity decrease. Because each question uses one feature at a time, its boundaries are made "
     "of horizontal and vertical steps, which is awkward for a diagonal relationship. Single trees "
     "are also unstable: change a few rows and you can get a visibly different tree."),

    ("Gini impurity",
     "Gini impurity measures how mixed a group is. The formula is one minus the sum of squared "
     "class fractions. Zero means the group is pure, all one class, while zero point five means an "
     "even fifty fifty mix. A tree picks the split that most reduces impurity. For a group that is "
     "nine tenths one class and one tenth the other, the impurity is one minus zero point eight one "
     "minus zero point zero one, which is zero point one eight, so it is fairly pure. To score a "
     "candidate split, the tree takes the impurity of each child group and averages them weighted "
     "by how many rows fell into each, then subtracts that from the parent's impurity. The result "
     "is the impurity decrease, and the winning question is the one with the largest decrease. "
     "Entropy is an alternative measure that behaves very similarly in practice; Gini is the "
     "default mostly because it is cheaper to compute."),

    ("Random forest",
     "A random forest grows many decision trees, each on a random sample of rows and features, "
     "then lets them vote. Because the trees make different mistakes, the errors cancel out and "
     "the forest generalises better than any single tree. This trick is called bagging. The row "
     "sample is drawn with replacement, so a given tree sees roughly two thirds of the rows and the "
     "leftover third can be used as a free validation set, known as the out-of-bag score. The "
     "feature sampling at each split is the extra ingredient that makes it a forest rather than "
     "plain bagging: it stops every tree from leaning on the same one dominant column, which keeps "
     "the trees genuinely different. More trees never hurt accuracy, they only cost time, so a few "
     "hundred is a sensible default and there is no need to tune that number carefully. The price "
     "is interpretability: you can no longer read the model as a single flowchart, only summarise "
     "it through feature importance."),

    ("Feature importance",
     "Feature importance ranks how much each column contributed to a tree model's decisions, by "
     "totalling the impurity reduction from every split that used it. It turns a model into a "
     "story you can tell, for example distance and preparation time drove most predictions. Read "
     "it with two warnings in mind. First, this impurity-based version is biased toward columns "
     "with many distinct values, such as identifiers or continuous measurements, because they offer "
     "more places to split. Second, when two columns carry the same information the model uses one "
     "and the other looks worthless, which does not mean it is. Permutation importance is a "
     "sturdier alternative: shuffle one column, see how much the score drops, and repeat. Above all, "
     "importance is not causation. It tells you what the model leaned on, not what causes the "
     "outcome in the world."),

    ("k-means clustering",
     "k-means is unsupervised, meaning it has no labels. It places k centres at random, assigns "
     "every point to its nearest centre, moves each centre to the average of its points, and "
     "repeats until nothing moves. It minimises inertia, the total squared distance to centres. "
     "Because the starting positions are random, two runs can land on different answers, so it is "
     "run several times over and the best result kept, and smarter starting positions known as "
     "k-means plus plus are used by default. Since it works by distance it needs scaling first, or "
     "whichever column has the biggest numbers will decide the clusters on its own. Its blind spot "
     "is shape: it looks for round, similarly sized blobs, so long thin clusters or one huge group "
     "beside a tiny one will be split badly. It also always returns exactly k clusters, even when "
     "the data has no groups at all, so the labels it gives you are a proposal to be sanity-checked, "
     "not a discovery."),

    ("Choosing k",
     "To choose the number of clusters, use the elbow method, where you plot inertia against k and "
     "look for the bend, and the silhouette score, which rates how cleanly separated the clusters "
     "are from minus one to plus one. When they disagree, you decide using domain knowledge. "
     "Inertia always falls as k rises, all the way to zero when every point is its own cluster, "
     "which is why you look for the bend rather than the minimum. Silhouette compares each point's "
     "distance to its own cluster against the nearest other cluster: above about zero point five is "
     "a solid structure, near zero means the clusters overlap, and negative means points are sitting "
     "in the wrong one. Neither method gives a right answer, because there usually is not one. The "
     "practical question is what the clusters are for, and three segments a marketing team can act "
     "on beat nine that score slightly better and describe nothing."),

    ("Feature engineering",
     "Feature engineering means creating better input columns, such as ratios, differences or date "
     "parts. A model can only use what you give it. Adding one good column can help far more than "
     "switching to a fancier model. Common moves are a ratio like price per square metre, a "
     "difference like days between order and delivery, pulling hour, weekday and month out of a "
     "timestamp, grouped summaries like a customer's average past order, and simple counts like the "
     "length of a text field. The best ideas come from domain knowledge rather than from a "
     "technique, so ask someone who does the actual job what they would look at. Two cautions: any "
     "step that learns something from the data, such as a group average, must be fitted inside the "
     "Pipeline on the training fold only, or you have created leakage; and a column built from "
     "information you would not have at prediction time is useless no matter how well it scores."),

    ("Scaling",
     "Standard scaling rewrites each value as z equals x minus the mean divided by the standard "
     "deviation. Distance-based models such as logistic regression, k-means and neural networks "
     "need it, because otherwise a large-valued column dominates. Trees and forests do not need it. "
     "After scaling, every column has mean zero and standard deviation one, so a value of two means "
     "two standard deviations above average. Min-max scaling is the other common choice and squeezes "
     "everything into zero to one, which is tidier but far more sensitive to a single extreme "
     "outlier. The rule that matters most is that the mean and standard deviation are learned from "
     "the training data only and then applied unchanged to the test data, which is exactly what "
     "putting the scaler in a Pipeline guarantees. Scaling changes the numbers, not the ordering or "
     "the information, so it can never hurt a tree, it is simply pointless there."),

    ("One-hot encoding",
     "One-hot encoding turns a text column into one zero-or-one column per category. You must not "
     "simply number the categories one, two, three, because that invents a false ordering that the "
     "model would wrongly trust. A colour column holding red, green and blue becomes three columns, "
     "with a single one marking which applies to each row. Two practical problems come up. A "
     "category the encoder never saw during training will appear at prediction time, so tell the "
     "encoder to ignore unknowns rather than crash. And a high-cardinality column such as postcode "
     "will explode into thousands of mostly empty columns, in which case group the rare values into "
     "an other bucket or encode by a summary statistic instead. Numbering categories is legitimate "
     "in one case only: when the order is real, such as small, medium and large, and that is called "
     "ordinal encoding."),

    ("The neuron",
     "A neuron does two steps. First a weighted sum of its inputs plus a bias, and then an "
     "activation function that bends the result. A single neuron with a sigmoid activation is "
     "exactly logistic regression. The weights say how much each input matters and can be negative, "
     "meaning that input pushes the answer down. The bias shifts the whole result up or down and "
     "lets the neuron fire even when every input is zero. A neuron with ten inputs therefore has "
     "eleven numbers to learn, ten weights and one bias, and those numbers are the only thing "
     "training changes. Everything else about a network follows from repeating this one small unit: "
     "the power comes not from any single neuron being clever, but from stacking many of them so "
     "that later ones work on what earlier ones produced."),

    ("Activation functions",
     "An activation adds a bend so a network can do more than draw a straight line. Sigmoid "
     "squashes any number into zero to one and suits a final probability. ReLU is max of zero and "
     "x, and is the usual choice inside hidden layers. Without any activation, stacking layers is "
     "pointless, because a chain of weighted sums collapses into one weighted sum and you are back "
     "to a straight line however many layers you added. Sigmoid has a weakness inside deep networks: "
     "for large positive or negative inputs it flattens out, the slope goes to almost nothing, and "
     "learning stalls, which is why it lost its place in hidden layers. ReLU keeps a constant slope "
     "for positive values so signals pass through cleanly, though a neuron that only ever receives "
     "negatives outputs zero forever and effectively dies. For the output layer, pick by the task: "
     "sigmoid for yes-or-no, softmax for several mutually exclusive classes, and nothing at all when "
     "predicting a plain number."),

    ("Neural network layers",
     "A network stacks neurons into layers: an input layer, one or more hidden layers, and an "
     "output layer. Hidden layers build their own features from the raw inputs, which is why a "
     "network can learn a curved boundary that a straight line cannot. Width is how many neurons "
     "sit in a layer and depth is how many layers there are. Every neuron in one layer connects to "
     "every neuron in the next, so the count of weights grows quickly: a layer of thirty-two "
     "feeding a layer of sixteen already carries over five hundred of them. This is where feature "
     "engineering is done for you, at the cost of no longer being able to say what any single "
     "hidden neuron represents. In principle one hidden layer that is wide enough can approximate "
     "almost any relationship, but in practice several moderate layers learn more easily than one "
     "enormous one. Start small, because a network with far more weights than you have rows will "
     "memorise them."),

    ("Training a network",
     "Training repeats four steps: a forward pass to get a prediction, a loss to measure how wrong "
     "it is, backpropagation to find which weights caused the error, and gradient descent to nudge "
     "each weight a small step downhill. Repeat thousands of times. The weights start as small "
     "random numbers, never all zero, because identical neurons would stay identical forever. One "
     "full sweep through the training data is an epoch, and within an epoch the data is processed "
     "in small batches so weights update many times per pass rather than once. The loss is chosen "
     "to match the task: cross-entropy for classification, mean squared error for regression. "
     "Backpropagation is just the chain rule applied backwards through the layers, working out each "
     "weight's share of the blame. Plain gradient descent works, but adaptive optimisers such as "
     "Adam adjust the step size per weight and usually converge faster with less fuss."),

    ("Learning rate",
     "The learning rate is the step size in gradient descent, written new weight equals old weight "
     "minus rate times slope. Too small and training crawls and never arrives. Too big and it "
     "overshoots and the loss bounces instead of falling. It is the single setting most worth "
     "getting right, and the loss curve tells you which way to move: a curve falling steadily is "
     "healthy, one that is nearly flat means the rate is too small, and one that jumps around or "
     "runs off to infinity means it is too large. Around zero point zero zero one is a common "
     "starting point for Adam, and it is usually tuned by trying values ten times apart rather than "
     "by small adjustments. A common refinement is to schedule it, starting larger to cover ground "
     "quickly and shrinking it later so the model can settle precisely instead of stepping over the "
     "spot it was heading for."),

    ("Early stopping",
     "Early stopping holds out a small validation slice during training and halts when that score "
     "stops improving. It prevents the network from carrying on into memorisation, shrinking the "
     "train-test gap and saving a lot of training time. The pattern it exploits is that training "
     "loss keeps falling essentially forever while validation loss falls, flattens, and then turns "
     "back up, and that turning point is the moment to stop. Because the curve is noisy, you do not "
     "stop at the first bad epoch: you allow a patience of several epochs without improvement, and "
     "you restore the weights from the best epoch rather than keeping the final ones, which are by "
     "then slightly worse. This validation slice is carved out of the training data, never from the "
     "test set. It is the easiest form of regularisation to add, since it needs no change to the "
     "model at all."),

    ("Bag of words",
     "Bag of words turns text into numbers by giving each vocabulary word a column and counting "
     "occurrences. It works surprisingly well, but it throws away word order, so the phrase not "
     "good looks almost identical to good. The vocabulary is built from the training documents, so "
     "any word appearing only at prediction time is simply dropped. The resulting table has one "
     "column per distinct word and is overwhelmingly zeros, which is why it is stored as a sparse "
     "matrix that records only the non-zero entries. Three settings do most of the tidying: "
     "removing stop words such as the and of, ignoring words that appear in fewer than a handful of "
     "documents, and ignoring words that appear in nearly all of them. Counting pairs of adjacent "
     "words as well as single words, known as bigrams, recovers a little of the lost order and "
     "rescues phrases like not good, at the cost of a much larger vocabulary."),

    ("TF-IDF",
     "TF-IDF weights each word by how often it appears in a document times how rare it is across "
     "all documents. Common words such as the get crushed toward zero because they carry little "
     "meaning, while distinctive words get boosted. The rarity part is the logarithm of the total "
     "number of documents divided by the number containing the word, so a word in every document "
     "scores about zero and a word in a handful scores high. Rows are then normalised to unit "
     "length, which means a long document and a short one about the same subject end up pointing "
     "the same way instead of the long one simply having bigger numbers. Like bag of words it "
     "ignores word order and treats different words as unrelated, so good and great share nothing. "
     "The document frequencies are learned from the training set only, which is why the vectoriser "
     "belongs inside a Pipeline."),

    ("Embeddings",
     "An embedding represents a word or document as a short list of numbers, positioned so that "
     "similar meanings sit close together. Unlike bag of words, it captures that good and great are "
     "related. Relationships become arithmetic, for example king minus man plus woman equals queen. "
     "The vector is dense, with every position holding a real number, and short, typically from "
     "fifty up to a couple of thousand values, against the tens of thousands of mostly-zero columns "
     "TF-IDF produces. The individual positions have no names and cannot be read; only the "
     "directions and distances between vectors mean anything. They can be produced by reducing a "
     "TF-IDF matrix with something like truncated SVD, which is the classic approach and needs a "
     "decent number of documents to find real structure, or taken from a model trained on huge "
     "amounts of text, which understands far more than your own corpus could teach it. Whatever "
     "produces them, every document and every query must go through the same embedder, or the "
     "numbers are not comparable."),

    ("Cosine similarity",
     "Cosine similarity compares the direction of two vectors, computed as their dot product "
     "divided by both their lengths. One means the same meaning, zero means unrelated. We use "
     "direction rather than distance so document length does not matter. Because it is the cosine "
     "of the angle between them, it ranges from minus one to one in general, though with word "
     "counts, which are never negative, it cannot fall below zero; embeddings from a dimensionality "
     "reduction do contain negative values, so scores below zero are possible there. A useful "
     "shortcut is to normalise every vector to unit length in advance, after which the dot product "
     "alone is the cosine similarity, and scoring a whole collection becomes one matrix "
     "multiplication. One trap is worth knowing: an all-zero vector, which is what you get when a "
     "query shares no vocabulary with the corpus, scores zero against everything, so a ranking will "
     "still be returned and it will be meaningless."),

    ("Semantic search",
     "Semantic search embeds every document once, embeds the incoming query the same way, scores "
     "each document by cosine similarity, and returns the highest scoring ones. It finds matches by "
     "meaning rather than by exact keyword. The stored document vectors are the index, and they are "
     "computed once ahead of time so that answering a query costs only one embedding plus a "
     "multiplication. Two practical details decide whether it works well. Long documents should be "
     "cut into paragraph-sized chunks before embedding, because one vector for a whole document "
     "blurs its separate ideas together and a specific question then matches nothing sharply. And a "
     "minimum score is worth enforcing, so that a query about something the collection does not "
     "cover returns nothing instead of the three least-bad matches presented as answers. Keyword "
     "search remains better at exact names, codes and rare terms, so the two are often combined. "
     "Feeding the retrieved passages to a language model to write the final answer is what people "
     "call retrieval-augmented generation."),
]


if __name__ == "__main__":
    print(f"{len(NOTES)} course notes in the knowledge base")
    words = sum(len(body.split()) for _, body in NOTES)
    print(f"{words} words total, about {words // len(NOTES)} per note")
    for title, _ in NOTES[:5]:
        print(" -", title)