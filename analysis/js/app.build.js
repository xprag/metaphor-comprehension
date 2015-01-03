({
    mainConfigFile: 'main.js',
    name: 'main',
    out: 'main.min.js',
    preserveLicenseComments: false,
    optimize: 'uglify2',
    paths: {
        requireLib: '../bower_components/requirejs/require'
    },
    include: 'requireLib'
})
