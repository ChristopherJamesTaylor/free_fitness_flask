const env = process.env;

const getDomainEnv = (function(){
    switch (env.FF_ENV){
        case 'local':
            return '//127.0.0.1';
        case 'dev':
        case 'stg':
            return `//${env.FF_ENV}.freefitness.dev`;
        default:
        case 'live':
            return '//freefitness.dev';
    }
});

module.exports = {
    api_url: getDomainEnv(),
};