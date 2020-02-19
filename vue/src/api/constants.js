const env = process.env;

const getDomainEnv = (function(){
    // eslint-disable-next-line no-console
    console.log("This is the environment ",env.FF_ENV);
    switch (env.FF_ENV){
        default:
        case 'local':
            return 'http://localhost:5000';
        case 'dev':
        case 'stg':
            return `//${env.FF_ENV}.freefitness.dev`;
        case 'live':
            return '//freefitness.dev';
    }
});

module.exports = {
    api_url: getDomainEnv(),
};