# Collaborative-filtering-based-recommender-systems-using-Pareto-dominance
    Recommend er Systems (RS) are responsible for providing users with a series of personalised suggestions (recommenda- tions) for certain types of items. RS extract the user’s relevant characterist ics and determine the subset of items that may be of interest to them.
    The way RS work can differ to a great extent depending on the types of items to be recommended and the available infor-mation about the user’s preferenc es. Therefore, RS must be able to use different mechanism s to obtain the most promising items for each user. RS are commonly called ‘‘filters’’ because they act as such.
    This projet is basically based on Collaborative FIltering.
    CF suffers from two main interrelated problems:
    •  It requires a large enough database to
    guarantee the correct process to search for similar users and to make the recommendati ons. 
    • The rating matrix is typically excessively sparse, which makes it difficult to calculate the similarity between pairs of users and reduces the accuracy of the computed recomme ndations.
  
    we present a method that improves CF prediction and recommend ation quality measures.

# Working
    Following three step summarised the whole process.
    • Find the k users most similar to the active user (the k-neighbours of the active user). This phase has the most             significant impact on the quality of the recommend ations. The method proposed in this paper provides a novel approach for obtaining a suitable set of neighbours to the active user.
    • Predict the rating that the active user would give to items they have not yet rated, by observing the ratings of their k-neighbours. When trying to predict an item’s value, there will normally be a significant number of neighbou rs who have not rated the item; therefore, mechanisms must be defined that enable the k-neighbours ’ ratings to be combined satisfactorily.
    • Find the most suitable N items to be recomme nded (due to their high rating, novelty, etc.).
