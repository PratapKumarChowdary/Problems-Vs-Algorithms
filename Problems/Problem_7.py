#!/usr/bin/env python
# coding: utf-8

# # Problem 7 - HTTPRouter using a Trie

# In[278]:


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie(root_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        parts_of_path = self.split_path(path)
        return self.route.insert(parts_of_path, handler)
        

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        parts_of_path = self.split_path(path)
        
        handler = self.route.find(parts_of_path)
        
        if handler:
            return self.route.find(parts_of_path)
        else:
            return "not found handler"


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        split = path.split('/')
        
        # If path is the root path than it returns ['/'] without any splitting
        if len(split) == 1 and split[0] == '/':
            return [""]
    
        # If path is not the root node than 
        # split the path by using '/' as separator
        # and remove the empty strings from the splitted list
        # by removing the empty strings we can handle trailing slashes
        parts_of_path = list()
    
        for i in split:
            if not i == "":
                parts_of_path.append(i)
                
        return parts_of_path


# In[279]:


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, parts_of_path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        
        current_node = self.root
    
        for part in parts_of_path:
            if part not in current_node.children:
                current_node.insert(part)
            current_node = current_node.children[part]
        current_node.handler = handler

    def find(self, parts_of_path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        
        for part in parts_of_path:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path):
        # Insert the node as before
        self.children[path] = RouteTrieNode(None)


# # Test Cases

# In[280]:


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/me", "about me handler")

# some lookups with the expected output
print("Path: / " + "-"*10 + " Handler: " + router.lookup("/")) # should print 'root handler'
print("Path: /home " +  "-"*10 + " Handler: " + router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print("Path: /home/about " + "-"*10 + " Handler: " + router.lookup("/home/about")) # should print 'about handler'
print("Path: /home/about/ " + "-"*10 + " Handler: " + router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print("Path: /home/about/me " + "-"*10 + " Handler: " + router.lookup("/home/about/me")) # should print 'about me handler'


# # Edge Test Cases

# In[281]:


# without '/' in starting of path
router.add_handler("a","a handler")
print("Path: / " + "-"*10 + " Handler: " + router.lookup(""))
print("Path: a " + "-"*10 + " Handler: " + router.lookup("a"))
print()
router.add_handler("a/b","a/b handler")
print("Path: a/b " + "-"*10 + " Handler: " + router.lookup("a/b"))


# In[282]:


# Change the root handler
router.add_handler("","new root handler")
print("Path: / " + "-"*10 + " Handler: " + router.lookup("/")) # should print 'root handler'
print("Path: /home " +  "-"*10 + " Handler: " + router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print("Path: /home/about " + "-"*10 + " Handler: " + router.lookup("/home/about")) # should print 'about handler'
print("Path: /home/about/ " + "-"*10 + " Handler: " + router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print("Path: /home/about/me " + "-"*10 + " Handler: " + router.lookup("/home/about/me")) # should print 'about me handler'


# In[283]:


# Adding Empty handler
router.add_handler("/","")
print("Path: / " + "-"*10 + " Handler: " + router.lookup("/")) # should print 'not found handler'

print()
# Requests for root - '' or '/' 
router.add_handler("/", "brand new root handler")
print("Path: / " + "-"*10 + " Handler: " + router.lookup("/")) # should print 'root handler'
print("Path: '' " + "-"*10 + " Handler: " + router.lookup("")) # should print 'root handler'


# In[284]:


# Large Path Input
capital_letters = [chr(x) for x in range(65, 91)]
small_letters = [chr(x) for x in range(97, 123)]
alphabets = capital_letters + small_letters

path = "/".join(alphabets)
print(path)

router.add_handler(path, "alphabets handler")

print("Path: / " + "-"*10 + " Handler: " + router.lookup("/"))
print("Path: /home " + "-"*10 + " Handler: " + router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print("Path: /home/about " + "-"*10 + " Handler: " + router.lookup("/home/about")) # should print 'about handler'
print("Path: /home/about/ " + "-"*10 + " Handler: " + router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print("Path: /home/about/me " + "-"*10 + " Handler: " + router.lookup("/home/about/me")) # should print 'about me handler'
print(f"Path: {path} " + "-"*20 + " Handler: " + router.lookup(path))

