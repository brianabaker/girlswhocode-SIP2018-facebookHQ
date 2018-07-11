const App = (function() {
  return class App {
    static init() {
      console.log("Running app");
      this.renderTodos();
      let form = document.getElementById("todo-form");
      form.addEventListener("submit", this.handleSubmit);

      /// presumably the app already has todos
      /// lets show some todos on the page

      /// 1. get the list from html
    }

    static renderTodos() {
      let todoContainer = document.getElementById("todo-list");
      // const todos = [{ title: "Wash Cat" }, { title: "Walk Fish" }];

      /// First send a GET request to http://localhost:3000
      /// response gives us some json
      /// json will be array
      /// iterate through array
      /// create todo objs
      /// append todo objs to screen


      TodoApi.fetchTodos().then(todos => {
        todos.forEach(function(todoJSON){
          let todo = new Todo(todoJSON)
          todoContainer.append(todo.render())
        })
      });
      //
    }

    static handleSubmit(event) {
      event.preventDefault();
      let formInput = document.getElementById("todo-input");

      // YOUR TODO
      // Fetch request and THEN upon receiving a response
      // render the todo on the page
      TodoApi.createTodo(formInput.value)
      .then(json => {
          let todoContainer = document.getElementById("todo-list");
          let todo = new Todo(json);
          todoContainer.append(todo.render());
      })
    }
  };
})();
