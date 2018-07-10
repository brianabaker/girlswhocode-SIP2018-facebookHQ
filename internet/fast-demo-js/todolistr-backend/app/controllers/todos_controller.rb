class TodosController < ApplicationController
  def index
    @todos = Todo.all
    render json:@todos
  end

  def create
    @todo = Todo.create(content: params[:content])
    render json: @todo
  end
end
