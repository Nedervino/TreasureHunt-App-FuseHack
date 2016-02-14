angular.module('app.controllers', [])

.controller('loginCtrl', function($scope, $http, $location, $ionicHistory) {
  $scope.data = {};

  $scope.submit = function(){
    window.localStorage['username'] = $scope.data.username;
    window.localStorage['phonenumber'] = $scope.data.phonenumber;

    var link = 'https://xmarksthespot.localtunnel.me/add_player';

    $http.post(link, {username : $scope.data.username, phonenumber : $scope.data.phonenumber}).then(function (res){
      $scope.response = res.data.players;
    });

    $ionicHistory.nextViewOptions({
      disableBack: true
    });

    $location.path('/gamesetup');
  };
})

.controller('gameSetupCtrl', function($scope, $ionicHistory, $location) {
  $scope.gotocreate = function(){
    $ionicHistory.nextViewOptions({
      disableBack: true
    });

    $location.path('/gamesetup2');
  }
  $scope.gotojoin = function(){
    $ionicHistory.nextViewOptions({
      disableBack: true
    });

    $location.path('/gamelobby');
  }
  $scope.gotorandomjoin = function(){
    $ionicHistory.nextViewOptions({
      disableBack: true
    });

    $location.path('/gamelobby');
  }

})

.controller('gameSetup2Ctrl', function($scope, $ionicHistory, $location) {
  $scope.start = function(){
    $ionicHistory.nextViewOptions({
      disableBack: true
    });

    $location.path('/playerinvite');
  }
})

.controller('gAMETITLECtrl', function($scope, $ionicHistory, $location, $http) {
  $scope.ready = function(){
    if (document.getElementById("readybutton").innerHTML == "Start game!") {
      $ionicHistory.nextViewOptions({
        disableBack: true
      });

      $location.path('/objectives');
    }
  }


  var submit = function() {
    var link = 'https://xmarksthespot.localtunnel.me/game_info';
    $http.post(link, {empty : "fissaman"}).then(function (res){
      $scope.response = res.data.started;
      if (res.data.started) {
        document.getElementById("readybutton").innerHTML = "Start game!";
      } else {
        document.getElementById("readybutton").innerHTML = "Please wait for instructions";
        setTimeout((function (){submit();}), 500);
      }
    })
  }

  submit();
})

.controller('objectivesCtrl', function($scope, $http, $location, $ionicHistory) {
  var keypadpoll = function() {
    $ionicHistory.nextViewOptions({
      disableBack: true
    });
    var link = 'https://xmarksthespot.localtunnel.me/objectives';
    $http.post(link, {username : window.localStorage['username']}).then(function (res){
      var response = res.data;
      var keypadavailable = response.available;
      if (keypadavailable) {
        $location.path('/keypad')
      } else {
        setTimeout((function (){keypadpoll();}), 500);
      }
    })
  }

  $scope.poll = function() {
    $ionicHistory.nextViewOptions({
      disableBack: true
    });
    var link = 'https://xmarksthespot.localtunnel.me/objectives';
    $http.post(link, {username : window.localStorage['username']}).then(function (res){
      var response = res.data;
      var objectives = response.objectives;
      var keypadavailable = response.available;
      if (keypadavailable) {
        $location.path('/keypad')
      } else {
        var htmlline = "";
        for (i = 0; i < objectives.length; i++) {
          if (i == 0) {
            doc = document.getElementById("nr1")
            doc.innerHTML = objectives[i].title;
            if (objectives[i].completed) {
              doc.style.color = "#80ff80";
            } else {
              doc.style.color = "white";
            }
          } else if (i == 1) {
            doc = document.getElementById("nr2")
            doc.innerHTML = objectives[i].title;
            if (objectives[i].completed) {
              doc.style.color = "#80ff80";
            } else {
              doc.style.color = "white";
            }
          } else if (i == 2){
            doc = document.getElementById("nr3")
            doc.innerHTML = objectives[i].title;
            if (objectives[i].completed) {
              doc.style.color = "#80ff80";
            } else {
              doc.style.color = "white";
            }
          }
        }
      }
    })
  }

  $scope.poll();
  keypadpoll();
})

.controller('invitePlayersCtrl', function($scope, $ionicHistory, $location) {
  $scope.inviteall = function(){
    $ionicHistory.nextViewOptions({
      disableBack: true
    });

    $location.path('/gamelobby');
  }
  $scope.invite = function(){

  }
})

.controller('keypadCtrl', function($scope, $ionicHistory, $http, $location) {
  $scope.data = {};

  $scope.submit = function(){
    var link = 'https://xmarksthespot.localtunnel.me/try_objective';

    $http.post(link, {username : window.localStorage['username'], objective : "entercode", code : $scope.data.code}).then(function (res){

    });

    $ionicHistory.nextViewOptions({
      disableBack: true
    });

    $location.path('/objectives');
  };
})
