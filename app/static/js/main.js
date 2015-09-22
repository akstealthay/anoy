
$(document).ready(function(){
    context.attach('span', [
        {text: 'Add another tag', href: '#'},
        {text: 'Delete all tags', href: '#'},
    ]);
});

$(document).ready(function() {

    var tagapi       = new tagapiClass('#content');
    var uiModules    = new uiModulesClass();

    var loadInIDProfiles = function(result) {
        $('#profiles').html(null);
        $.each(result, function(profileName, tags) {
            $('#profiles').append($('<option>').html(profileName));
        });
    }

    var loadProfileInfo = function(profileName) {
        uiModules.showWaiting($('#tags'));
        // load tags
        $.get( '/data/profile/' + profileName.trim(), function( response ) {
        
            if (response.error) {
                uiModules.showError(response);
                uiModules.removeWaiting($('#tags'));
                return;
            }

            var tags = response.response;
            var listTags = $('<ul>').addClass('tags');
            $.each(tags, function(index, tag) {
                listTags.append($('<li>').addClass('tag').html(tag));
            });
            $('#tags').html(listTags);

            uiModules.updateContextMenu();
        });
    }

    var loadProfile = function(profileName) {
        $('#current-profile-name').html(profileName);
        $('#profiles').val(profileName);

        loadProfileInfo(profileName);
    }

    var loadProfileNames = function(callback) {
        $.get( '/data/profile', function( result ) {
            if (result.error) {
                uiModules.showError(result);
                return;
            }
            callback(result.response);
        });
    }

    $('#profiles').change(function() {
        loadProfile(this.value.trim());
    });

    $("#add-profile-form").submit(function(e) {
        e.preventDefault();

        var profileName = $('#new-profile-entry').val().trim();

        tagapi.addProfile(profileName);

    });

    $("#add-tag-form").submit(function(e) {
        e.preventDefault();

        var tagName = $('#new-tag-entry').val().trim();
        var profileName = $('#current-profile-name').html().trim();

        tagapi.addTag(tagName, profileName);
    });

    $("#load-file-form").submit(function(e) {
        e.preventDefault();

        /* Loads the file into #content region */
        var filePath = $('#file-path').val().trim();

        if (!filePath) {
            alert('Please enter a file path');
            return;
        }

        uiModules.showWaiting($('#content'));

        $.get( '/load', {file_path:filePath}, function( result ) {
            if( result.error ) {
                uiModules.showError(result);
                uiModules.removeWaiting($('#content'));
                return;
            }

            var fileContents = result.response.raw;
            tagapi.setRawContent(fileContents);
        });

    });

    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });

    // init function
    var init = function() {
        // Put all profile in combobox
        loadProfileNames(function(result) {
            loadInIDProfiles(result);
        });

        $.get('/data/current_profile', function(response) {
            if(response.error) {
                uiModules.showError(response);
                return;
            }
            var profileName = response.response;
            loadProfile(profileName);
        });

        context.init({
            fadeSpeed: 100,
            filter: function ($obj){},
            above: 'auto',
            preventDoubleContext: true,
            compress: false
        });
    }
    init();
});