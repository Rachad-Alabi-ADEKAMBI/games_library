<template>
    <div class="jumbotron vertical-center bg-light">
      <div class="container">
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.1/cerulean/bootstrap.min.css"
          integrity="sha512-uYdFW1wYPUqMECgTumIJgmAh/sHPOKHY6RBhItyI46XW/uJIiS/l6hsSPDrpnDxTlpj6/9gJIzyO0c3+1iwBfA=="
          crossorigin="anonymous"
          referrerpolicy="no-referrer"
        />
        <div class="row">
          <div class="col-sm-12">
            <h1 class="text text-center bg-primary text-white" style="border-radius: 10px;">Games library</h1>
            <hr />
            <br />
            <!--alert msg-->

            <button type="button" class="btn btn-success btn-sm" v-b-modal.game-modal>
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
                      <b-button class="btn btn-info btn-sm">Update</b-button>
                      <b-button class="btn btn-danger btn-sm">Delete</b-button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>

            <footer class="footer bg-primary text-white text-center" style="border-radius: 10px;" >Copyright  &Copy;. all right reserved 2023</footer>
          </div>
        </div>
      </div>
    </div>

    <!--first model-->
    <b-modal  v-if="showAddForm" ref="addGameModal" id="game-modal"
    title="Add a new game" hide-backdrop hide-footer>
        <!--<b-form @submit="onS  ubmit" @reset="onReset" class="w-100">
          <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
            <b-form-input id="form-title-input" type="text" v-model="addGameForm.title" placeholder="Enter game" required></b-form-input>
          </b-form-group>

          <b-form-group id="form-genre-group" label="Genre:" label-for="form-genre-input">
            <b-form-input id="form-genre-input" type="text" v-model="addGameForm.genre" placeholder="Enter genre" required></b-form-input>
          </b-form-group>

          <b-form-group id="form-played-group" label="Played:" label-for="form-played-input">
            <b-form-checkbox v-model="addGameForm.played">Played</b-form-checkbox>
          </b-form-group>

          <b-button variant="outline-info" type="submit">Submit</b-button>
          <b-button variant="outline-danger" type="reset">Reset</b-button>
        </b-form>-->
        uhuibilbhi
  </b-modal>






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
            showAddForm: false
        },
        games: []
      };
    },
    methods: {
      getGames() {
        const path = 'http://localhost:5000/games';
        axios
          .get(path)
          .then((res) => {
            console.log(res.data);
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
            this.addGameForm.title ='',
            this.addGameForm.genre ='',
            this.addGameForm.played = []
      },
      onsubmit(e){
        e.preventDefault();
        this.$refs.addGameModal.hide();
        let played = false;
        if (this.addGameForm.played[0]) payload = true;
        const payload = {
            title: this.addGameForm.title,
            genre: this.addGameForm.genre,
            played,

        };
        this.addGame(payload);
        this.initForm;
      },
      displayAddForm(){
        this.showAddForm = true;
      },
      closeAddForm(){
        this.showAddForm = false;
      }
    },
    created() {
      this.getGames();
    }
  }
  </script>