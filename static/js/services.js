var Suite101 = angular.module('Experience', ['ngResource']).
        factory('Experience', function($resource) {
    return $resource('api/experiences/:experiencesID', {}, {
        update: {method:'PUT'}
    });
});

Suite101.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/experiences', {templateUrl: 'partials/experience-list.html',   controller: ExperienceListCtrl}).
        when('/experiences/:experiencesID', {templateUrl: 'partials/experience-detail.html', controller: ExperienceDetailCtrl}).
        otherwise({redirectTo: '/experiences'});
}]);