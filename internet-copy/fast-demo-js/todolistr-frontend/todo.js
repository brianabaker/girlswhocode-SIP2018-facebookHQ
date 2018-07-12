const Todo = (function() {
  return class Todo {
    constructor({ content }) {
      this.content = content;
    }

    renderHTML() {
      let todoItem = document.createElement("li");
      let todoText = document.createTextNode(this.content);
      todoItem.append(todoText);
      return todoItem;
    }

    render() {
      return this.renderHTML();
    }
  };
})();
