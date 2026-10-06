# VehicleServiceCollectionSdk C# SDK 1.0.0

Welcome to the VehicleServiceCollectionSdk SDK documentation. This guide will help you get started with integrating and using the VehicleServiceCollectionSdk SDK in your project.

## Versions

- SDK version: `1.0.0`

## Table of Contents

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Authentication](#authentication)
  - [API Key Authentication](#api-key-authentication)
- [Setting a Custom Timeout](#setting-a-custom-timeout)
- [Sample Usage](#sample-usage)
- [Services](#services)
- [Models](#models)

# Setup & Configuration

## Supported Language Versions

This SDK is compatible with the following versions: `C# >= .NET 6`

## Installation

To get started with the SDK, we recommend installing using `nuget`:

```bash
dotnet add package VehicleServiceCollectionSdk
```

## Authentication

### API Key Authentication

The VehicleServiceCollectionSdk API uses API keys as a form of authentication. An API key is a unique identifier used to authenticate a user, developer, or a program that is calling the API.

#### Setting the API key

When you initialize the SDK, you can set the API key as follows:

```cs
using VehicleServiceCollectionSdk;
using VehicleServiceCollectionSdk.Config;

var config = new VehicleServiceCollectionSdkConfig()
{
	ApiKeyAuth = new ApiKeyAuthConfig("YOUR_API_KEY")
};

var client = new VehicleServiceCollectionSdkClient(config);
```

If you need to set or update the API key after initializing the SDK, you can use:

```cs
client.SetApiKey("YOUR_API_KEY")
```

## Setting a Custom Timeout

You can set a custom timeout for the SDK's HTTP requests as follows:

```cs
client.SetTimeout(TimeSpan.FromSeconds(10))
```

# Sample Usage

Below is a comprehensive example demonstrating how to authenticate and call a simple endpoint:

```cs
using VehicleServiceCollectionSdk;
using VehicleServiceCollectionSdk.Config;
using Environment = VehicleServiceCollectionSdk.Http.Environment;

var apiKeyConfig = new ApiKeyAuthConfig("YOUR_API_KEY");

var config = new VehicleServiceCollectionSdkConfig
{
  ApiKeyAuth = apiKeyConfig
};

var client = new VehicleServiceCollectionSdkClient(config);

var response = await client.VehicleServiceCollectionSdk.GetAllVehiclesAsync();

Console.WriteLine(response);

```

## Services

The SDK provides various services to interact with the API.

Below is a list of all available services:

| Name                                                                                               |
| :------------------------------------------------------------------------------------------------- |
| [VehicleServiceCollectionSdkService](documentation/services/VehicleServiceCollectionSdkService.md) |

## Models

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

Below is a list of all available models:

| Name                                                                   | Description |
| :--------------------------------------------------------------------- | :---------- |
| [CreateAVehicleRequest](documentation/models/CreateAVehicleRequest.md) |             |
