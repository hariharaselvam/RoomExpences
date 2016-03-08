window.appName="RuckusWireless"
window[appName] = angular.module(appName, ['ui.router']);
//var host = location.hostname;
//appName = "https://localhost:5001/";
window[appName].config(function($stateProvider, $urlRouterProvider,$httpProvider) {
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('dashboard', {
            url: '/',
            templateUrl: 'Ruckus_Pages/Dashboard.html',
//            controller: 'monitoring_dashboard_controller',
        });
	 $stateProvider
        .state('controller', {
            url: '/controller',
            templateUrl: 'Ruckus_Pages/Controller.html',
//            controller: 'monitoring_controller',
        });
	 $stateProvider
        .state('events', {
            url: '/events',
            templateUrl: 'modules/events/events.html',
            controller: 'events_controller',
        });


});
