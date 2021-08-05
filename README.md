# Sveno
### Description
Sveno is a component transpiler that transform React components to Svelte components. It only works on simple small non-library components so far, but more updates are coming.

Sveno aims to become a powerfull tool able to transpile complete projects, and to help developpers discover the advantages of using Svelte.

![React to Svelte](react-to-svelte.png)

### Why use Svelte
While React is a library that adds extra weight to your code base and uses a virtual DOM, Svelte compiles it's files to ideal javascript, thus reducing the actual weight. As a result, Svelte is significantly faster than any framework or library using virtual DOMs.

[Learn more here](https://svelte.dev/blog/virtual-dom-is-pure-overhead)

### Setup

You'll need [Python3](https://www.python.org/downloads/) and [pip3](https://pip.pypa.io/en/stable/getting-started/) installed.
Install the requirements with `pip3 install -r ./src/requirements.txt`<br/>
Congratz \\(^o^)/ ! You're ready to go!

### Usage

The program takes 2 arguments: the react source folder and a svelte destination folder

`python3  ./src/main.py react_source_folder svelte_destination_folder`

### How does it work

1. The program looks through each file, starting from the source root folder, that has a `.js` or a `.jsx` extension. Style files with `.css`  extension are also taken into account and can be integrated into the correct svelte component.
2. Using a set of regex (regular expressions), key elements are gathered and stored into dataclasses. [Try some regex here.](https://regex101.com/)
3. Dataclasses are the main element that will be worked upon. Class Components, Functionnal Components, Variables, and other important pieces of code have their own dataclass. They are used to access information and transform syntactic elements from react to svelte syntax. Some elements are substituted while others are simply deleted (eg: `this.props.name` will become `name`)
4. New files and folders are created. Because React files can contain multiple components, contrarly to Svelte files, each component will be translated into a new file of the same name. They will be contained in a folder bearing the name of the initial react file.<br>For example, a file named `actions.jsx` and containing 2 components named `simpleAction` and `doubleAction` will result in a folder named `actions` with two svelte files named `simpleAction.svelte` and `doubleAction.svelte`
5. Components are written in the new files, using the dataclasses and corresponding templates.


## Functionnalities
As of today, the following elements can be transpiled:
* Functionnal components
* Class components
* 'Classic' functions
* Props
* Class Lifecycle methods (ComponentWillMount, ComponentDidMount, ComponentDidUpdate, GetSnapshotBeforeUpdate)
* UseEffect (The functionnal component LifeCycle hook)
* SetState, UseState, this.state - initialize and set variable values
* Events (onClick, onMouseMove, etc)

## Upcoming
* ReactDOM.render() and entrypoint
* Better utilitary files handling
* Loops
* Conditions
* Routing

## Contributors:
- [Allan Deleve](https://github.com/Gfaim)
- [Amoz Pay](https://github.com/amozpay)
- [Baptiste Barbotin](https://github.com/barbo69)
- [Tom Chaveau](https://github.com/TomChv)
