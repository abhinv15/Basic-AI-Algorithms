#adverserial search algorithm

#MIN_MAX
def min_max(node,tree,is_maximizing):
    if isinstance(tree[node],int):
        print(f"Leaf node {node} with value {tree[node]}")
        return tree[node],node
    print(f"exploring the node {node}")

    if is_maximizing:
        best_value = float('-inf')
        best_path = []
        for child in tree[node]:
            value,path = min_max(child,tree,False)
            if value > best_value:
                best_value = value
                best_path = [node] + path
    else:
        best_value = float('inf')
        best_path  = []
        for child in tree[node]:
            value,path = min_max(child,tree,True)
            if value < best_value:
                best_value = value
                best_path = [node] + path
    print(f"{node} has the value {best_value}")
    return best_value,best_path

#alpha beta pruning
def alpha_beta_prun(node,tree,alpha,beta,is_maximizing):
    if isinstance(tree[node],int):
        print(f"Leaf node {node} with value {tree[node]}")
        return tree[node],node
    print(f"Exploring the node {node} with alpha = {alpha}, beta = {beta}")

    if is_maximizing:
        best_value = float('-inf')
        best_path = []
        for child in tree[node]:
            value,path = alpha_beta_prun(child,tree,alpha,beta,False)
            if value > best_value:
                best_value = value
                best_path = [node] + path
            alpha = max(best_value,alpha)
            print(f"Node {node} updates alpha to {alpha}")
            if alpha >= beta:
                print(f"Pruning occur at node {node}")
                break
    else:
        best_value = float('inf')
        best_path = []
        for child in tree[node]:
            value,path = alpha_beta_prun(child,tree,alpha,beta,True)
            if value < best_value:
                best_value = value
                best_path = [node] + path
            beta = min(best_value,beta)
            print(f"Node {node} updates beta value to {beta}")
            if alpha >= beta:
                print(f"Pruning occur at node {node}")
                break

    print(f"{node} has the value {best_value}")
    return best_value,best_path



    