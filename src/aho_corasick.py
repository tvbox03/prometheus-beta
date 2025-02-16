from collections import defaultdict, deque

class AhoCorasick:
    def __init__(self, patterns):
        """
        Initialize the Aho-Corasick algorithm with a list of patterns to match.
        
        :param patterns: List of strings to search for
        """
        self.patterns = patterns
        self.goto = {}  # Goto function (transitions)
        self.fail = {}  # Failure function 
        self.output = defaultdict(list)  # Output function (matched patterns)
        self._build_automaton()

    def _build_automaton(self):
        """
        Construct the Aho-Corasick automaton using pattern construction 
        and failure link construction.
        """
        # Goto transitions (Trie construction)
        for pattern in self.patterns:
            current = 0
            for char in pattern:
                if current not in self.goto:
                    self.goto[current] = {}
                if char not in self.goto[current]:
                    # Generate a new state
                    self.goto[current][char] = len(self.goto)
                current = self.goto[current][char]
            
            # Mark the end of a pattern with its full text
            self.output[current].append(pattern)

        # Failure function construction (BFS)
        self.fail[0] = 0
        queue = deque()

        # Initialize first level
        for char, state in self.goto.get(0, {}).items():
            queue.append(state)
            self.fail[state] = 0

        # BFS to construct failure links
        while queue:
            current = queue.popleft()
            
            # For each possible character transition from current state
            for char, next_state in self.goto.get(current, {}).items():
                queue.append(next_state)
                
                # Find the longest proper suffix
                state = self.fail[current]
                while state > 0 and char not in self.goto.get(state, {}):
                    state = self.fail[state]
                
                # Set failure link
                if char in self.goto.get(state, {}):
                    self.fail[next_state] = self.goto[state][char]
                else:
                    self.fail[next_state] = 0
                
                # Combine output with failure link's output
                self.output[next_state].extend(self.output[self.fail[next_state]])

    def search(self, text):
        """
        Search for all occurrences of patterns in the given text.
        
        :param text: Input text to search
        :return: List of tuples (pattern, start_index)
        """
        results = []
        current = 0

        for i, char in enumerate(text):
            # Follow goto and fail transitions
            while current > 0 and char not in self.goto.get(current, {}):
                current = self.fail[current]
            
            # Move to next state
            if char in self.goto.get(current, {}):
                current = self.goto[current][char]
            
            # Check for matches at current state
            for pattern in self.output.get(current, []):
                results.append((pattern, i - len(pattern) + 1))

        return results