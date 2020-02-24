const env = process.env;

const getDomainEnv = (function(){
    if (!env.FF_ENV) {
        env.FF_ENV = env.NODE_ENV;
    }

    // eslint-disable-next-line no-console
    console.log("This is the environment ",env.FF_ENV);
    switch (env.FF_ENV) {
        case 'local':
            return 'http://localhost:5000';
        case 'dev':
        case 'stg':
            return `//${env.FF_ENV}.freefitness.dev/api`;
        default:
        case 'live':
        case 'production':
            return '//freefitness.dev/api';
    }
});

module.exports = {
    api_url: getDomainEnv(),
};
