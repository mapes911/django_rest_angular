var Suite101 = angular.module('Suite101', ['ngResource']).
        factory('Experience', function($resource) {
    return $resource('api/experiences/:experiencesID', {}, {
        query: {method:'GET', params:{experiencesID:''}, isArray:false}
    });
});

Suite101.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/e/:experiencesID', {templateUrl: 'partials/experience-detail.html', controller: ExperienceDetailCtrl}).
        otherwise({redirectTo: '/'});
}]);