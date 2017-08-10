from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):
    result = [hypothesis] # add the hypothesis to the result
    
    for rule in rules: # check every rule
    
        consequent = rule.consequent() # get the "thens"
        
        for expr in consequent: # for every "then"
        
            bindings = match(expr, hypothesis) # get the variables that match 
                                               # a "then" to the hypothesis
            
            if bindings or expr == hypothesis: # if there is an exact match to
                                               # the "then" or the "then" is of the
                                               # same form
                                               
                antecedent = rule.antecedent() # get the "ifs"
                
                if isinstance(antecedent, str): # if the "if" is not an AND/OR
                
                    new_hypothesis = populate(antecedent, bindings) # bind the "ifs" to the
                                                                     # variables we collected
                                                                     # to make new "thens"
                                                                     
                    result.append(new_hypothesis) # add the new "thens" to result
                    
                    result.append(backchain_to_goal_tree(rules, new_hypothesis)) # backchain the new "thens"
                else: # this means that the "if" is an AND/OR
                    statements = [populate(ante_expr, bindings) for ante_expr in antecedent] # add every item in the list
                                                                                             # bound with the variables we collected
                    
                    new_results = [] # create list for backchained items from statements
                    
                    for statement in statements: # iterate through statements
                    
                        new_results.append(backchain_to_goal_tree(rules, statement)) # add the backchained items from statements to new_results
                        
                    result.append(create_statement(new_results, antecedent)) # use create statement to turn these results into AND/OR and add to result
                    
    return simplify(OR(result)) # simplify the result
    
def create_statement(statements, rule):
    if isinstance(rule, AND):
        return AND(statements)
    elif isinstance(rule, OR):
        return OR(statements)
            

# Here's an example of running the backward chainer - uncomment
# it to see it work:
print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')
