/**
 * Created by hariharaselvam on 11/12/16.
 */
//var appName = 'Wakeup';
window.appName = "Wakeup";
window[appName] = angular.module(appName, ['ui.router', 'ngSanitize']);

window[appName].config(function ($stateProvider, $urlRouterProvider, $httpProvider) {


    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('dashboard', {
            url: '/',
            templateUrl: '/media/js/modules/dashboard.html',
            controller: 'dashboard_controller'
        });


    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

window[appName].controller('wakeup_controller', function ($rootScope, $scope, $state, http ) {

    $rootScope.title = "Wakeup";

    http.Requests("get","/api/ui/session/","").success(function (response) {
        $rootScope.user = response;

    });


});
