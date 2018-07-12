const TodoApi = (function() {
  return class TodoApi {
    static fetchTodos() {
      return fetch("http://localhost:10524/todos")
      .then(res => res.json())
      // .then(json => console.log(json))
    }

    static createTodo(todoText){
      return fetch("http://localhost:10524/todos",{
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          content: todoText
        })
      })
      .then(res => res.json())
    }
  };
})();


// rails s -p 10524
