$(document).ready(function() {

    var showError = function(response) {
        alert(response.error);
    };

    var showWaiting = function(targetElement) {
        targetElement.html('<i class="fa fa-spinner fa-spin"></i>');
    }

    var removeWaiting = function(targetElement) {
        targetElement.html(null);
    }

    var loadInIDProfiles = function(result) {
        $('#profiles').html(null);
        $.each(result, function(profileName, tags) {
            $('#profiles').append($('<option>').html(profileName));
        });
    }

    var loadProfileInfo = function(profileName) {
        showWaiting($('#tags'));
        // load tags
        $.get( '/data/profile/' + profileName.trim(), function( response ) {
        
            if (response.error) {
                showError(response);
                removeWaiting($('#tags'));
                return;
            }

            var tags = response.response;
            var listTags = $('<ul>').addClass('tags');
            $.each(tags, function(index, tag) {
                listTags.append($('<li>').addClass('tag').html(tag));
            });
            $('#tags').html(listTags);
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
                showError(result);
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
        if (!profileName) {
            alert('Please enter name of the profile');
            return;
        }

        $.post( "/act/" + profileName, {action:'add'},function( response ) {
            if (response.error) {
                showError(response);
                return;
            }
            $('#profiles').append($('<option>').html(profileName));
            $('#new-profile-entry').val(null);
            alert('Profile added successfully');
        });

    });

    $("#add-tag-form").submit(function(e) {
        e.preventDefault();

        var tagName = $('#new-tag-entry').val().trim();
        var profileName = $('#current-profile-name').html().trim();

        if (!tagName) {
            alert('Please enter appropriate value of the tag');
            return;
        }

        if (!profileName) {
            alert('No profile selected. Select a profile first.');
            return;
        }

        $.post( "/act/" + profileName + '/' + tagName, {action:'add'},function( response ) {
            if (response.error) {
                showError(response);
                return;
            }

            $('#new-tag-entry').val(null);
            $('#tags ul').append($('<li>').addClass('tag').html(tagName));
            alert('Tag ' + tagName + ' added successfully to profile ' + profileName);
        });
    });

    $("#load-file-form").submit(function(e) {
        e.preventDefault();

        /* Loads the file into #content region */
        var filePath = $('#file-path').val().trim();

        if (!filePath) {
            alert('Please enter a file path');
            return;
        }

        showWaiting($('#content'));

        $.get( '/load', {file_path:filePath}, function( result ) {
            if( result.error ) {
                showError(result);
                removeWaiting($('#content'));
                return;
            }
            $("#content").html(result.response.raw);
        });

    });

    $('#content').mouseup(function() {
        console.log('Mouse Up' + window.getSelection());
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
                showError(response);
                return;
            }
            var profileName = response.response;
            loadProfile(profileName);
        });
    }
    init();
});