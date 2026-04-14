---
title: RestClient
date: 2026-03-03 16:00:09
tags: 
categories: 
---


💠

- 1. [RestClient](#restclient)

💠 2026-03-03 16:00:09
****************************************
# RestClient
Spring6.1+ 

```java
    ClientHttpRequestFactorySettings settings = ClientHttpRequestFactorySettings.defaults()
            .withConnectTimeout(Duration.ofSeconds(5))
            .withReadTimeout(Duration.ofSeconds(10));

    this.restClient = RestClient.builder()
            .requestFactory(ClientHttpRequestFactoryBuilder.detect().build(settings))
            .defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
            .build();
```