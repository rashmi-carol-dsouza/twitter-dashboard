CREATE TABLE tweet
(
    id VARCHAR(300) PRIMARY KEY,
    tweet_time NVARCHAR(max) NOT NULL,
    tweet_text NVARCHAR(max) NOT NULL,
    sentiment NVARCHAR(max),
    topic NVARCHAR(max),
    latitude NVARCHAR(max),
    longitude NVARCHAR(max)
);