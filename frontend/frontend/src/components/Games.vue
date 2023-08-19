<template>
    <div class="jumbotron vertical-center bg-light mt-3">

    </div>

    <div class="container">
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.1/cerulean/bootstrap.min.css"
          integrity="sha512-uYdFW1wYPUqMECgTumIJgmAh/sHPOKHY6RBhItyI46XW/uJIiS/l6hsSPDrpnDxTlpj6/9gJIzyO0c3+1iwBfA=="
          crossorigin="anonymous"
          referrerpolicy="no-referrer"
        />

        <div class="row">
          <div class="col-sm-12 col-md-" v-if="success" ></div>
        </div>
        <div class="row" v-if="showAddForm">
          <div  class="col-sm-12 col-md-6 p-3 mt-3 mx-auto" role="dialog">
                            <div class="modal-dialog card">

                                <div class="modal-content">
                                        <div class="modal-header">
                                            <h3  class="modal-title text mx-auto">
                                                Add new book
                                            </h3>
                                        </div>

                                        <div class="model-body">
                                                  <form action="" method="POST">
                                                    <div class="row">
                                                         <div class="col-sm-12 col-md-10 mx-auto text-left left ">
                                                          <label for="" class="text text-left mb-1">Enter game: </label> <br>
                                                          <input type="text"  v-model="addGameForm.title"  required>
                                                         </div>
                                                  </div>

                                                  <div class="row mt-2">
                                                         <div class="col-sm-12 col-md-10 mx-auto text-left left ">
                                                          <label for="" class="text text-left mb-1">Enter genre: </label> <br>
                                                          <input type="text"  v-model="addGameForm.genre"
                                                           required>
                                                         </div>
                                                  </div>

                                                  <div class="row mt-2">
                                                         <div class="col-sm-12 col-md-12 mx-left text-left">
                                                          <label for="" class="text text-left mb-1">Played: </label>
                                                          <input type="checkbox" v-model="addGameForm.played"  >
                                                         </div>
                                                  </div>

                                                  <div class="row mt-3">
                                                      <div class="col-4 mx-auto text-center">
                                                           <button class="btn btn-success mx-auto"  @click="submit()"
                                                            type="submit">Submit</button>
                                                      </div>

                                                      <div class="col-4 mx-auto text-center mx-auto">
                                                        <button class="btn btn-warning" @click="" type="submit">Reset</button>
                                                      </div>
                                                  </div>
                                                  </form>
                                        </div>

                                        <div class="modal-footer mt-3 m-2">
                                            <button class="btn btn-secondary" data-dismiss="modal"  @click="closeAddForm()" >
                                                Close
                                            </button>
                                        </div>
                                </div>

                            </div>
              </div>
        </div>

        <div class="row" v-if="showUpdateForm">
          <div  class="col-sm-12 col-md-6 p-3 mt-3 mx-auto" role="dialog">
                            <div class="modal-dialog card">

                                <div class="modal-content">
                                        <div class="modal-header">
                                            <h3  class="modal-title text mx-auto">
                                                Update
                                            </h3>
                                        </div>

                                        <div class="model-body">
                                                  <form action="" method="">
                                                    <div class="row">
                                                         <div class="col-sm-12 col-md-10 mx-auto text-left left ">
                                                          <label for="" class="text text-left mb-1">Enter game: </label> <br>
                                                          <input type="text"  v-model="addGameForm.title"  required>
                                                         </div>
                                                  </div>

                                                  <div class="row mt-2">
                                                         <div class="col-sm-12 col-md-10 mx-auto text-left left ">
                                                          <label for="" class="text text-left mb-1">Enter genre: </label> <br>
                                                          <input type="text"  v-model="addGameForm.genre"
                                                           required>
                                                         </div>
                                                  </div>

                                                  <div class="row mt-2">
                                                         <div class="col-sm-12 col-md-12 mx-left text-left">
                                                          <label for="" class="text text-left mb-1">Played: </label> <br>
                                                          <select  v-model="addGameForm.played" id="">
                                                              <option value="">Please select</option>
                                                              <option value="Yes">Yes</option>
                                                              <option value="No">No</option>
                                                          </select>
                                                         </div>
                                                  </div>

                                                  <div class="row mt-3">
                                                      <div class="col-4 mx-auto text-center">
                                                           <button class="btn btn-success mx-auto"  @click="" type="submit">Update</button>
                                                      </div>

                                                      <div class="col-4 mx-auto text-center mx-auto">
                                                        <button class="btn btn-warning" @click="" type="submit">Reset</button>
                                                      </div>
                                                  </div>
                                                  </form>
                                        </div>

                                        <div class="modal-footer mt-3 m-2">
                                            <button class="btn btn-secondary" data-dismiss="modal"  @click="closeAddForm()" >
                                                Close
                                            </button>
                                        </div>
                                </div>

                            </div>
              </div>
        </div>

         <div class="row" v-if="showDeleteForm">
          <div  class="col-sm-12 col-md-6 p-3 mt-3 mx-auto" role="dialog">
                            <div class="modal-dialog card">

                                <div class="modal-content">
                                        <div class="modal-header">
                                            <h3  class="modal-title text mx-auto">
                                                Delete game
                                            </h3>
                                        </div>

                                        <div class="model-body">
                                                  <form action="" method="">
                                                    <div class="row">
                                                         <div class="col-sm-12 col-md-10 mx-auto text-left left ">
                                                          <label for="" class="text text-left mb-1">Delete game: </label> <br>
                                                            <select name="" v-model="deleteGame" id="">
                                                               <option value="">Please <select name="" id=""></select></option>
                                                                <option value="yes">Yes</option>
                                                                <option value="No">No</option>
                                                            </select>
                                                         </div>
                                                  </div>

                                                  <div class="row mt-3">
                                                      <div class="col-4 mx-auto text-center">
                                                           <button class="btn btn-success mx-auto"  @click="" type="submit">Delete</button>
                                                      </div>

                                                      <div class="col-4 mx-auto text-center mx-auto">
                                                        <button class="btn btn-warning" @click="" type="submit">Reset</button>
                                                      </div>
                                                  </div>
                                                  </form>
                                        </div>

                                        <div class="modal-footer mt-3 m-2">
                                            <button class="btn btn-secondary" data-dismiss="modal"  @click="closeAddForm()" >
                                                Close
                                            </button>
                                        </div>
                                </div>

                            </div>
              </div>
        </div>

        <div class="row"  v-if="showGames">
          <div class="col-sm-12">
            <h1 class="text text-center bg-primary text-white" style="border-radius: 10px;">Games library</h1>
            <hr />
            <br />
            <!--alert msg-->

            <button type="button"  data-toggle="modal"
            data-target="myModal"
             class="btn btn-success btn-sm" @click="displayAddForm()">
              Add Game
            </button>
            <br /><br />


            <table class="table table-hover">
              <!--table head-->
              <thead>
                <tr>
                  <th scope="col">Title</th>
                  <th scope="col">Genre</th>
                  <th scope="col">Played ?</th>
                  <th scope="col">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(game, index) in games" :key="index">
                  <td>{{ game.title }}</td>
                  <td>{{ game.genre }}</td>
                  <td>
                    <span v-if="game.played"> Yes </span>
                    <span v-else> No </span>
                  </td>
                  <td>
                    <div class="btn-group" role="group">
                      <button class="btn btn-info btn-sm">Update</button>
                      <button class="btn btn-danger btn-sm">Delete</button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
           </div>
        </div>

        <div class="row mt-5">
          <footer class="footer bg-primary text-white text-center"
          style="border-radius: 10px;" >Copyright  & Copy; all right reserved 2023</footer>

        </div>
      </div>

                 <!--add-->



  </template>



  <script>
  import axios from 'axios';

  export default {
    name: 'Games',
    data() {
      return {
        msg: '',
        addGameForm: {
            title: '',
            genre: '',
            played: [],

        },
        showDeleteForm: false,
        games: [],
        showAddForm: false,
        showUpdateForm: false
      };
    },
    methods: {
      displayAddForm(){
        this.showAddForm = true;
        this.showUpdateForm = false;
        this.showGames = false;
      },
      closeAddForm(){
        this.showAddForm = false;
        this.showGames = true;
      },
      displayDeleteForm(){
        this.showDeleteForm = true;
        this.showUpdateForm = false;
        this.showGames = false;
      },
      closeDeleteForm(){
        this.showDeleteForm = false;
        this.showGames = true;
      },
      getGames() {
        const path = 'http://localhost:5000/games';
        this.showGames = true;
        axios
          .get(path)
          .then((res) => {
           // console.log(res.data);
            this.games = res.data.games; // Access the 'games' array inside the response data
          })
          .catch((err) => {
            console.error(err);
          });
      },
      addGame(payload){
        const path = 'http://localhost:5000/games';
        axios
          .get(path, payload)
          .then((res) => {
                this.getGames();
          })
          .catch((err) => {
            console.error(err);
          this.getGames();
          });
      },
      initForm(){
        this.addGameForm.title = '',
        this.addGameForm.genre = ''
        this.addGameForm.played = []
      },
      submit(){
          e.preventDefault();
          this.showAddForm = false;
          let played = false;
          if(this.addGameForm.played[0]) played = true;
          const payload = {
            title : this.addGameForm.title,
            genre : this.addGameForm.genre,
            played,
          };
          this.addGame(payload)
      },
    },
    created() {
      this.getGames();
    }
  }
  </script>

<style>
      .container{
        position: relative;
        height: auto;
        display: flex;
        flex-direction: column;
      }
      .table{
        bottom: 0;
      }
</style>