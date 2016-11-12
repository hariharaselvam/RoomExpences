/**
 * Created by hariharaselvam on 11/12/16.
 */
window[appName].controller('dashboard_controller', function ($rootScope, $scope, $state, http ) {

    $rootScope.title = "Dashboard";
    $scope.dashboard = {
        "page":"Dashboard"
    };

});