
module.exports = {
  networks: {
    development: {
      host: "192.168.43.135",     // Localhost (default: none)
      port: 7545,            // Standard Ethereum port (default: none)
      network_id: "*",       // Any network (default: none)
    },
  },
  contracts_build_directory: "./src/abis/",

  // Configure your compilers
  compilers: {
    solc: {

      // See the solidity docs for advice
      // about optimization and evmVersion
      optimizer: {
        enabled: false,
        runs: 200
      },
      evmVersion: "byzantium"
    }
  }
};