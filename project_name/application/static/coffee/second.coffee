class Test
    constructor: (selector)->
      selector.find('span').text('success').addClass "success"

