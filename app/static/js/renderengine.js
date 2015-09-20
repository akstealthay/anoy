var renderEngineClass = function() {
    /*
     *  RenderEngineClass: Class that defines render engine
     *  Contains all the methods required to render.
     *  
     *  A tag internally is stored as:
     *  ! TAG Format !
     *      [list_of_tags](actual text that is tagged)
     *      list_of_tags: profile#tag, profile#tag, ...
     *
     *  This is then parsed and converted to nested span tags
     *  processed with respect to tagRenderTemplate 
     */

    /* Constants */
    var tagRenderTemplate = '<span class="tag" profile-name="${profile}" tag-name="${tag}">${text}</span>';

    var tagFormatTemplate = '[${profiletag_list}](${text})'

    /* Public Methods */
    this.toHtml = function(rawContent) {
        /*
         * Converts string having "TAG" format to HTML
         *      1. Look for the TAG format in rawContent
         *      2. Replace it with tagRenderTemplate
         *
         *  In case of multiple tags, make tagRenderTemplate nested.
         */

        var htmlStrObj = {htmlStr:'', error:null} ;

        for ( var index = 0 ; index < rawContent.length ; index++ ) {
            var ch = rawContent.charAt(index);

            if ( ch == '[' ) {
                index = processPotentialTag(rawContent, index, htmlStrObj);
            }
            else {
                htmlStrObj.htmlStr += ch;
            }
        }
        return htmlStrObj.htmlStr;
    };

    this.toTag = function(htmlContent) {
        /*
         * Converts HTML string to "TAG" format
         *      1. Look for the span in htmlContent
         *      2. Replace it with tagFormat
         *
         *  In case of multiple tags, club all to one.
         */

        var tagStrObj = {tagStr:'', error:null};
        var wrapper= document.createElement('div');

        wrapper.innerHTML = htmlContent;

        var allNodes = wrapper.childNodes;

        for( var i = 0 ; i < allNodes.length ; i++ ) {
            tagStrObj.tagStr += getTagStr(allNodes[i]);
        }

        return tagStrObj.tagStr;   
    }


    /* Private Helper Methods */
    function getTagStr(node) {

        if(node.childElementCount == undefined) {
            return node.textContent;
        }

        var profileTagArray = [];

        while( node.childElementCount != undefined ) {
            profileTagArray.push(node.getAttribute('profile-name') + '#' + node.getAttribute('tag-name'));
            node = node.firstChild;
        }
        return '[' + profileTagArray.join(' ') + '](' + node.textContent + ')';
    }


    function processPotentialTag(rawContent, index, htmlStrObj) {
        /*
         *  Processes the potential tag.
         *  Returns the `index` from which iteration should resume.
         */

        var oldIndex = index;

        // Check if tag exists
        var isTagPresent = false;

        var countSquareBracket = 0;
        var countRoundBracket = 0;

        var tagsBuffer = '';
        var contentBuffer = '';

        for ( ; index < rawContent.length ; index++ ) {
            var ch = rawContent.charAt(index);
            if ( ch == '[' ) {
                countSquareBracket++;
            }
            else if ( ch == ']' ) {
                countSquareBracket--;
            }
            else {
                tagsBuffer += ch;
            }

            if( countSquareBracket == 0 ) {
                break;
            }

        }

        if ( countSquareBracket != 0 ) {
            /*
             *  Brackets did not end but string did
             *  Hence error
             */
             isTagPresent = false;
             htmlStrObj.error = 'Square Brackets did not end properly.'
             return oldIndex+1;
        }

        index++;

        if ( index < rawContent.length && rawContent.charAt(index) != '(' ) {
            /*
             *  No round bracket found after closing square bracket.
             *  Hence error
             */
             isTagPresent = false;
             htmlStrObj.error = 'No Round bracket found after closing square brackets.'
             return oldIndex+1;
        }

        // Round brackets does exist

        for ( ; index < rawContent.length ; index++ ) {
            var ch = rawContent.charAt(index);
            if ( ch == '(' ) {
                countRoundBracket++;
            }
            else if ( ch == ')' ) {
                countRoundBracket--;
            }
            
            // appending data to buffer
            contentBuffer += ch;
            
            if( countRoundBracket == 0 ) {
                break;
            }

        }

        if ( countRoundBracket != 0 ) {
            /*
             *  Brackets did not end but string did
             *  Hence error
             */
             isTagPresent = true;
             htmlStrObj.error = 'Round Brackets did not end properly but no worries :).'
             return index;
        }

        // Assert: All is well
        tagsArray = tagsBuffer.split(' ');

        contentBuffer = contentBuffer.slice(1, -1);

        var text = contentBuffer;

        for ( var i = 0 ; i < tagsArray.length ; i++ ) {
            if(tagsArray[i].length > 0) {
                var profileTag = tagsArray[i].split('#');
                text = tagRenderTemplate.replace('${profile}', profileTag[0])
                                 .replace('${tag}', profileTag[1])
                                 .replace('${text}', text);
            }
        }


        htmlStrObj.htmlStr += text;

        // If everything goes well then return the index of ')' so that
        // main for loop will do another index++ and everything goes well.
        return index;
    };
};