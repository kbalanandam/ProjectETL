CREATE TABLE vetaranplates (
  Id mediumint NOT NULL AUTO_INCREMENT,
  PlateState char(5) DEFAULT NULL,
  LicensePlate char(30) NOT NULL,
  StartEffectiveDate date DEFAULT NULL,
  EndEffectiveDate date DEFAULT NULL,
  CreatedDate datetime DEFAULT NULL,
  CreatedUser char(30) DEFAULT NULL,
  UpdatedDate datetime DEFAULT NULL,
  UpdatedUser char(30) DEFAULT NULL,
  PRIMARY KEY (Id)
);

