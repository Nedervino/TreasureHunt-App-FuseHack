angular.module('app.routes', [])

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider



    .state('login', {
      url: '/login',
      templateUrl: 'templates/login.html',
      controller: 'loginCtrl'
    })





    .state('gameSetup', {
      url: '/gamesetup',
      templateUrl: 'templates/gameSetup.html',
      controller: 'gameSetupCtrl'
    })





    .state('gameSetup2', {
      url: '/gamesetup2',
      templateUrl: 'templates/gameSetup2.html',
      controller: 'gameSetup2Ctrl'
    })





    .state('gAMETITLE', {
      url: '/gamelobby',
      templateUrl: 'templates/gAMETITLE.html',
      controller: 'gAMETITLECtrl'
    })





    .state('objectives', {
      url: '/objectives',
      templateUrl: 'templates/objectives.html',
      controller: 'objectivesCtrl'
    })





    .state('invitePlayers', {
      url: '/playerinvite',
      templateUrl: 'templates/invitePlayers.html',
      controller: 'invitePlayersCtrl'
    })



    .state('keypad', {
      url: '/keypad',
      templateUrl: 'templates/keypad.html',
      controller: 'keypadCtrl'
    })

    ;

  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/login');

});
