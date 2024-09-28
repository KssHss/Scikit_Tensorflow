# Fundamentals:  
ML is the field of study that gives the computer th eability to learn without being explicitly programmed.
A computer is said to learn from experience E with respect to task T and some performance measure P, if its performance on T, as measured by P, improves with experience E.  

examples that the system uses to learn --> trianing set  
each training example --> training instance or sample  
Spam filter: Performance measured as the ratio of correctly classified emails --> accuracy (used in classification tasks) 

<img width="513" alt="Captura de pantalla 2024-09-28 a las 11 22 13" src="https://github.com/user-attachments/assets/889a1e93-583d-4c27-a77c-fcc0babab0ae">

## Types of ML: 
* Whether or not they are trained with human supervision (supervised, unsuper‐ vised, semisupervised, and Reinforcement Learning) 
* Whether or not they can learn incrementally on the fly from a stream of incoming data (online versus batch learning) 
*  Whether they work by simply comparing new data points to known data points, or instead detect patterns in the training data and build a predictive model, much like scientists do (instance-based versus model-based learning) 

Can be combined: a state-of-the-art spam filter may learn on the fly using a deep neural network model trained using examples of spam and ham; this makes it an online, model- based, supervised learning system.

******************************************Supervised vs Unsupervised**********************************************
### Supervised: 
training data includes labels (desired solutions) or predictors.
:Typical tasks: classification, predict a target numeric value (regression)
Attribute is data type # feature ~ attribute + value (can be used interchangeably)

Most important algorithms:
• k-Nearest Neighbors  
• Linear Regression  
• Logistic Regression (commonly used for classification: it can output the probability of belonging to a given class)  
• Support Vector Machines (SVMs)  
• Decision Trees and Random Forests  
• Neural networks (can be unsupervised or semi)  

### Unsupervised:  
training data is unlabeled (blog's visitors into clusters)  

Most important algorithms:  
• Clustering
  — k-Means  
  — Hierarchical Cluster Analysis (HCA)  
  — Expectation Maximization
• Visualization and dimensionality reduction (to preserve as much structure as possible)  
  — Principal Component Analysis (PCA)  
  — Kernel PCA  
  — Locally-Linear Embedding (LLE)  
  — t-distributed Stochastic Neighbor Embedding (t-SNE)
• Association rule learning
  — Apriori 
  — Eclat

**dimensionality reduction**: to simplify the data without losing too much information. One way to do this is to merge several correla‐ ted features into one. For example, a car’s mileage may be very correlated with its age, so the dimensionality reduction algorithm will merge them into one feature that rep‐ resents the car’s wear and tear =>  feature extraction ==> less disk and memory => better perfom

**anomaly detection**: unsual credit card transactions. System is trained with normal instances, and when it sees a new instance it can tell whether it looks like a normal one or not.  

**Association rule learning**: to dig into large amounts of data and discover interesting relations between attributes. For example, suppose you own a supermarket. Running an association rule on your sales logs may reveal that people who purchase barbecue sauce and potato chips also tend to buy steak.

### Semisupervised:  
Algorithms that deal with partially labeled training data, usually a lot of unlabeled data and a little bit of labeled data such as photo-hosting services, such as Google Photos.  

Most semisupervised learning algorithms are combinations of unsupervised and supervised algorithms. For example, deep belief networks (DBNs) are based on unsu‐ pervised components called restricted Boltzmann machines (RBMs) stacked on top of one another. RBMs are trained sequentially in an unsupervised manner, and then the whole system is fine-tuned using supervised learning techniques.  

### Reinforcement Learning:
<img width="473" alt="Captura de pantalla 2024-09-28 a las 12 07 24" src="https://github.com/user-attachments/assets/82f837b3-4a11-4f24-8be5-9f352be8ac90">  

******************************************Batch vs Online Learning**********************************************
### Batch learning:  
the system is **incapable** of learning incrementally: it must be trained using all the available data. typically done offline (time and computing resources = $$$). In production it just applies what it has learned => __offline learning__  
if new data --> new version of the system from scratch on the full dataset (new + old data) to replace the new version.
for every week or every 24h.  

### Online learning:
you train the system incrementally by feeding it data instances sequentially, either individually or by small groups called mini-batches. Each learning step is fast and cheap, so the system can learn about new data on the fly, as it arrives.  
For systems that recieves datd as continuous flow (stock prices) and need to adapt to change rapidly. Once the system has learned about ne data instances --> they can be discarded  

Online learning algorithms can also be used to train systems on huge datasets that cannot fit in one machine’s main memory **out-of-core learning**. The algorithm loads part of the data, runs a training step on that data, and repeats the process until it has run on all of the data **¡¡usually this is done offline!!**  
Parameter for how fast online learining systems should adapt to changing data = learning rate  
__If you set a high learning rate, then your system will rapidly adapt to new data, but it will also tend to quickly forget the old data (you don’t want a spam filter to flag only the latest kinds of spam it was shown). Conversely, if you set a low learning rate, the system will have more inertia; that is, it will learn more slowly, but it will also be less sensitive to noise in the new data or to sequences of nonrepresentative data points.__  

Challenge: bad data ==> you need to monitor your system closely and promptly switch learning off (and possibly revert to a previously working state) if you detect a drop in performance. You may also want to monitor the input data and react to abnormal data (e.g., using an anomaly detection algorithm).

******************************************Instance vs Model-Based Learning**********************************************  

how they generalize to instances they never have seen before.(Good performance is good but TRUE GOAL IS TO PERFORM WELL ON NEW INSTANCES)  

### Instance-based learning:
the system learns the examples by heart, then generalizes to new cases using a similarity measure

### Model-based learning:  
to generalize from a set of examples is to build a model of these examples, then use that model to make predictions.  

# Challenges  












