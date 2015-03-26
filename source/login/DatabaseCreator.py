import os,sys
import subprocess
import MySQLdb
from PyQt4 import QtCore


class DatabaseCreator(object):
	def __init__(self,newDatabaseName,parent=None):
		self.si_om=parent
		self.newDatabaseName = newDatabaseName
		self.sqldump = """-- phpMyAdmin SQL Dump
		-- version 4.0.4
		-- http://www.phpmyadmin.net
		--
		-- Host: localhost
		-- Generation Time: Feb 06, 2015 at 10:47 PM
		-- Server version: 5.6.12-log
		-- PHP Version: 5.4.12

		SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
		SET time_zone = "+00:00";


		/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
		/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
		/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
		/*!40101 SET NAMES utf8 */;

		--
		-- Database: `"""+newDatabaseName+"""`
		--
		CREATE DATABASE IF NOT EXISTS `"""+newDatabaseName+"""` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
		USE `"""+newDatabaseName+"""`;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_bank`
		--

		CREATE TABLE IF NOT EXISTS `gd_bank` (
		`id` int(11) NOT NULL,
		  `kodeRekening` varchar(64) NOT NULL,
		  `nomorRekening` varchar(100) NOT NULL,
		  `anRekening` varchar(128) NOT NULL,
		  `cabangBank` varchar(128) NOT NULL,
		  `alamatBank` varchar(256) NOT NULL,
		  `kontakBank` varchar(64) NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_bank_keluar`
		--

		CREATE TABLE IF NOT EXISTS `gd_bank_keluar` (
		`id` int(11) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `nilaiTotal` double NOT NULL,
		  `noAkunBank` varchar(10) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_bank_masuk`
		--

		CREATE TABLE IF NOT EXISTS `gd_bank_masuk` (
		`id` int(11) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `nilaiTotal` double NOT NULL,
		  `noAkunBank` varchar(10) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_bayar`
		--

		CREATE TABLE IF NOT EXISTS `gd_bayar` (
		`id` int(11) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `kodeRekening` varchar(64) NOT NULL,
		  `jumlahDibayar` double NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_buku_besar`
		--

		CREATE TABLE IF NOT EXISTS `gd_buku_besar` (
		`id` int(11) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `noAkun` varchar(10) NOT NULL,
		  `debit` double NOT NULL,
		  `kredit` double NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_data_departemen`
		--

		CREATE TABLE IF NOT EXISTS `gd_data_departemen` (
		`id` int(11) NOT NULL,
		  `kodeDepartemen` varchar(64) NOT NULL,
		  `namaDepartemen` varchar(256) NOT NULL,
		  `parentDepartemen` varchar(64) NOT NULL,
		  `kodePenjab` varchar(64) NOT NULL,
		  `catatan` varchar(384) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_data_gudang`
		--

		CREATE TABLE IF NOT EXISTS `gd_data_gudang` (
		`id` int(11) NOT NULL,
		  `kodeGudang` varchar(64) NOT NULL,
		  `namaGudang` varchar(64) NOT NULL,
		  `lokasi` varchar(256) NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_data_pajak`
		--

		CREATE TABLE IF NOT EXISTS `gd_data_pajak` (
		`id` int(11) NOT NULL,
		  `kodePajak` varchar(64) NOT NULL,
		  `namaPajak` varchar(100) NOT NULL,
		  `persenPajak` double NOT NULL,
		  `keterangan` varchar(256) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_data_penyimpanan`
		--

		CREATE TABLE IF NOT EXISTS `gd_data_penyimpanan` (
		`id` int(11) NOT NULL,
		  `kodeBarang` varchar(64) NOT NULL,
		  `tanggalMasuk` date NOT NULL,
		  `hargaBeli` double NOT NULL,
		  `hargaJual` double NOT NULL,
		  `kodeGudang` varchar(64) NOT NULL,
		  `pemasok` varchar(64) NOT NULL,
		  `stok` int(11) NOT NULL,
		  `kurs` varchar(10) NOT NULL,
		  `saldoAwal` double NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_data_produk`
		--

		CREATE TABLE IF NOT EXISTS `gd_data_produk` (
		`id` int(11) NOT NULL,
		  `kodeBarang` varchar(64) NOT NULL,
		  `deskripsi` text NOT NULL,
		  `kodeSatuan` varchar(20) NOT NULL,
		  `hpp` double NOT NULL,
		  `namaBarang` varchar(100) NOT NULL,
		  `sifat` varchar(10) NOT NULL,
		  `stok` int(11) NOT NULL,
		  `noAkunPenjualan` varchar(10) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_detail_bank_keluar`
		--

		CREATE TABLE IF NOT EXISTS `gd_detail_bank_keluar` (
		`id` int(11) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `noAkunDetail` varchar(10) NOT NULL,
		  `nilaiDetail` double NOT NULL,
		  `catatan` varchar(512) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_detail_bank_masuk`
		--

		CREATE TABLE IF NOT EXISTS `gd_detail_bank_masuk` (
		`id` int(11) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `noAkunDetail` varchar(10) NOT NULL,
		  `nilaiDetail` double NOT NULL,
		  `catatan` varchar(512) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_detail_kas_keluar`
		--

		CREATE TABLE IF NOT EXISTS `gd_detail_kas_keluar` (
		`id` int(11) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `noAkunDetail` varchar(10) NOT NULL,
		  `nilaiDetail` double NOT NULL,
		  `catatan` varchar(512) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_detail_kas_masuk`
		--

		CREATE TABLE IF NOT EXISTS `gd_detail_kas_masuk` (
		`id` int(11) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `noAkunDetail` varchar(10) NOT NULL,
		  `nilaiDetail` double NOT NULL,
		  `catatan` varchar(512) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_detail_transaksi_jurnal`
		--

		CREATE TABLE IF NOT EXISTS `gd_detail_transaksi_jurnal` (
		`id` int(11) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `noAkunJurnal` varchar(10) NOT NULL,
		  `kodeDepartemen` varchar(64) NOT NULL,
		  `debit` double NOT NULL,
		  `kredit` double NOT NULL,
		  `tanggal` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
		) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_fase_proyek`
		--

		CREATE TABLE IF NOT EXISTS `gd_fase_proyek` (
		`id` int(11) NOT NULL,
		  `kodeProyek` varchar(64) NOT NULL,
		  `namaFase` varchar(128) NOT NULL,
		  `deskripsiFase` text NOT NULL,
		  `anggaranBiaya` double NOT NULL,
		  `realisasiBiaya` double NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_harta_tetap`
		--

		CREATE TABLE IF NOT EXISTS `gd_harta_tetap` (
		`id` int(11) NOT NULL,
		  `namaAset` varchar(128) NOT NULL,
		  `hargaBeli` double NOT NULL,
		  `umurEkonomis` int(11) NOT NULL,
		  `lastActivity` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
		  `noAkunAset` varchar(10) NOT NULL,
		  `noAkunPenyusutan` varchar(10) NOT NULL,
		  `tanggalBeli` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
		  `penyusutanBulan` double NOT NULL,
		  `terhitungTanggal` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
		  `bebanBulan` double NOT NULL,
		  `nilaiBuku` double NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_hutang`
		--

		CREATE TABLE IF NOT EXISTS `gd_hutang` (
		`id` int(11) NOT NULL,
		  `noInvoice` varchar(64) NOT NULL,
		  `noReferensi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `jumlahPenerimaan` double NOT NULL,
		  `jumlahTagihan` double NOT NULL,
		  `noAkunKas` varchar(10) NOT NULL,
		  `noAkunPiutang` varchar(10) NOT NULL,
		  `pembayaranKe` tinyint(4) NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_invoice_penjualan`
		--

		CREATE TABLE IF NOT EXISTS `gd_invoice_penjualan` (
		`id` int(11) NOT NULL,
		  `kodeTransaksi` varchar(10) NOT NULL,
		  `noSalesOrder` varchar(64) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `nilai` double NOT NULL,
		  `hargaPokok` double NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_jurnal_memorial`
		--

		CREATE TABLE IF NOT EXISTS `gd_jurnal_memorial` (
		`id` int(11) NOT NULL,
		  `noReferensi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `jumlahUang` double NOT NULL,
		  `noAkunPiutang` varchar(10) NOT NULL,
		  `noAkunMemorial` varchar(10) NOT NULL,
		  `tipe` tinyint(4) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_kas_keluar`
		--

		CREATE TABLE IF NOT EXISTS `gd_kas_keluar` (
		`id` int(11) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `nilaiTotal` double NOT NULL,
		  `noAkunKas` varchar(10) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_kas_masuk`
		--

		CREATE TABLE IF NOT EXISTS `gd_kas_masuk` (
		`id` int(11) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `nilaiTotal` double NOT NULL,
		  `noAkunKas` varchar(10) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_kelompok_barang`
		--

		CREATE TABLE IF NOT EXISTS `gd_kelompok_barang` (
		`id` int(11) NOT NULL,
		  `kodeKelompok` varchar(64) NOT NULL,
		  `namaKelompok` varchar(128) NOT NULL,
		  `noAkunHpp` varchar(8) NOT NULL,
		  `noAkunPenjualan` varchar(8) NOT NULL,
		  `noAkunPersediaan` varchar(8) NOT NULL,
		  `noAkunKonsinyasi` varchar(8) NOT NULL,
		  `noAkunReturPenjualan` varchar(8) NOT NULL,
		  `noAkunPengiriman` varchar(8) NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_kelompok_transaksi`
		--

		CREATE TABLE IF NOT EXISTS `gd_kelompok_transaksi` (
		`id` int(11) NOT NULL,
		  `kodeKelompok` varchar(2) NOT NULL,
		  `keterangan` varchar(128) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_klasifikasi`
		--

		CREATE TABLE IF NOT EXISTS `gd_klasifikasi` (
		`id` int(11) NOT NULL,
		  `noKlasifikasi` tinyint(4) NOT NULL,
		  `namaKlasifikasi` varchar(100) NOT NULL,
		  `namaAliasKlasifikasi` varchar(100) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_mata_uang`
		--

		CREATE TABLE IF NOT EXISTS `gd_mata_uang` (
		`id` int(11) NOT NULL,
		  `kodeMatauang` varchar(64) NOT NULL,
		  `namaMatauang` varchar(64) NOT NULL,
		  `simbol` varchar(5) NOT NULL,
		  `kursTukar` double NOT NULL DEFAULT '1',
		  `isDefault` tinyint(1) NOT NULL DEFAULT '0'
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_nama_alamat`
		--

		CREATE TABLE IF NOT EXISTS `gd_nama_alamat` (
		`id` int(11) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `namaPelanggan` varchar(256) NOT NULL,
		  `tipe` varchar(32) NOT NULL,
		  `npwp` varchar(64) NOT NULL,
		  `diskon` double NOT NULL,
		  `jatuhtempo` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
		  `diskonAwal` double NOT NULL,
		  `dendaKeterlambatan` int(11) NOT NULL,
		  `alamat` varchar(512) NOT NULL,
		  `kontak` varchar(64) NOT NULL,
		  `noAkunPiutang` varchar(10) NOT NULL,
		  `noAkunHutang` double NOT NULL,
		  `saldo` double NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_order_pembelian`
		--

		CREATE TABLE IF NOT EXISTS `gd_order_pembelian` (
		`id` int(11) NOT NULL,
		  `noAkunPembelian` varchar(10) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `kodeBarang` varchar(64) NOT NULL,
		  `jumlah` int(11) NOT NULL,
		  `harga` double NOT NULL,
		  `diskom` double NOT NULL,
		  `kodePajak` varchar(64) NOT NULL,
		  `retur` int(11) NOT NULL,
		  `isDibayar` tinyint(1) NOT NULL DEFAULT '0',
		  `isDikirim` tinyint(1) NOT NULL DEFAULT '0',
		  `kodeMatauang` varchar(64) NOT NULL,
		  `JumlahDibayar` double NOT NULL,
		  `kodeTOS` varchar(64) NOT NULL,
		  `kodeTOP` varchar(64) NOT NULL,
		  `biayaKirim` double NOT NULL,
		  `alamatKirim` varchar(512) NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_order_penjualan`
		--

		CREATE TABLE IF NOT EXISTS `gd_order_penjualan` (
		`id` int(11) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `kodeBarang` varchar(64) NOT NULL,
		  `kodeSatuan` varchar(64) NOT NULL,
		  `jumlah` double NOT NULL,
		  `hargaJual` double NOT NULL,
		  `hpp` double NOT NULL,
		  `disc` double NOT NULL,
		  `total` double NOT NULL,
		  `pajak` double NOT NULL,
		  `totalPajak` double NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_pembelian_barang`
		--

		CREATE TABLE IF NOT EXISTS `gd_pembelian_barang` (
		`id` int(11) NOT NULL,
		  `noInvoice` varchar(64) DEFAULT NULL,
		  `noPO` varchar(64) DEFAULT NULL,
		  `namaBarang` varchar(128) NOT NULL,
		  `kodeVendor` varchar(64) NOT NULL,
		  `hargaBarang` double NOT NULL,
		  `jumlahBarang` double NOT NULL,
		  `satuan` varchar(64) NOT NULL,
		  `totalHarga` double NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_periode_akuntansi`
		--

		CREATE TABLE IF NOT EXISTS `gd_periode_akuntansi` (
		`id` int(11) NOT NULL,
		  `kodePerusahaan` varchar(64) NOT NULL,
		  `bulan` tinyint(4) NOT NULL,
		  `tahun` smallint(6) NOT NULL,
		  `bulanTutupBuku` tinyint(4) NOT NULL,
		  `kodeDepartemen` varchar(64) NOT NULL,
		  `namaDepartemen` varchar(64) NOT NULL,
		  `prefix` varchar(16) NOT NULL,
		  `format` varchar(32) NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_piutang`
		--

		CREATE TABLE IF NOT EXISTS `gd_piutang` (
		`id` int(11) NOT NULL,
		  `noInvoice` varchar(64) NOT NULL,
		  `noReferensi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `jumlahPenerimaan` double NOT NULL,
		  `jumlahTagihan` double NOT NULL,
		  `noAkunKas` varchar(10) NOT NULL,
		  `noAkunPiutang` varchar(10) NOT NULL,
		  `pembayaranKe` tinyint(4) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_proyek`
		--

		CREATE TABLE IF NOT EXISTS `gd_proyek` (
		`id` int(11) NOT NULL,
		  `kodeProyek` varchar(64) NOT NULL,
		  `namaProyek` varchar(128) NOT NULL,
		  `kodePenjab` varchar(64) NOT NULL,
		  `progress` double NOT NULL,
		  `tanggalMulai` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
		  `tanggalSelesai` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
		  `anggaranTotal` double NOT NULL,
		  `realisasiTotal` double NOT NULL,
		  `isFase` tinyint(1) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_rekening_jurnal`
		--

		CREATE TABLE IF NOT EXISTS `gd_rekening_jurnal` (
		`id` int(11) NOT NULL,
		  `noAkun` varchar(8) NOT NULL,
		  `namaAkun` varchar(200) NOT NULL,
		  `namaAliasAkun` varchar(200) NOT NULL,
		  `saldoAwal` double NOT NULL,
		  `saldoSekarang` double NOT NULL,
		  `isKas` tinyint(2) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_satuan_pengukuran`
		--

		CREATE TABLE IF NOT EXISTS `gd_satuan_pengukuran` (
		`id` int(11) NOT NULL,
		  `kodeSatuan` varchar(64) NOT NULL,
		  `namaSatuan` varchar(64) NOT NULL,
		  `keterangan` varchar(128) NOT NULL,
		  `faktorPengali` double NOT NULL DEFAULT '0',
		  `kodeSatuanParent` varchar(64) DEFAULT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_tabel_info_perusahaan`
		--

		CREATE TABLE IF NOT EXISTS `gd_tabel_info_perusahaan` (
		`id` int(11) NOT NULL,
		  `kodePerusahaan` varchar(64) NOT NULL,
		  `namaPerusahaan` varchar(100) NOT NULL,
		  `alamat` varchar(512) NOT NULL,
		  `kota` varchar(64) NOT NULL,
		  `negara` varchar(64) NOT NULL,
		  `kodePos` varchar(16) NOT NULL,
		  `telp` varchar(16) NOT NULL,
		  `email` varchar(32) NOT NULL,
		  `web` varchar(32) NOT NULL,
		  `jenisUsaha` varchar(32) NOT NULL,
		  `kodeMatauang` int(11) NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_top`
		--

		CREATE TABLE IF NOT EXISTS `gd_top` (
		`id` int(11) NOT NULL,
		  `kodeTOP` varchar(64) NOT NULL,
		  `namaTOP` varchar(64) NOT NULL,
		  `isiTOP` text NOT NULL,
		  `keterangan` varchar(512) NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_tos`
		--

		CREATE TABLE IF NOT EXISTS `gd_tos` (
		`id` int(11) NOT NULL,
		  `kodeTOS` varchar(64) NOT NULL,
		  `namaTOS` varchar(64) NOT NULL,
		  `isiTOS` text NOT NULL,
		  `keterangan` varchar(512) NOT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_transaksi_jurnal`
		--

		CREATE TABLE IF NOT EXISTS `gd_transaksi_jurnal` (
		`id` int(11) NOT NULL,
		  `kodeTransaksi` varchar(64) NOT NULL,
		  `catatan` varchar(256) NOT NULL,
		  `nilaiTransaksi` double NOT NULL,
		  `tanggal` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
		) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_uang_muka`
		--

		CREATE TABLE IF NOT EXISTS `gd_uang_muka` (
		`id` int(11) NOT NULL,
		  `noReferensi` varchar(64) NOT NULL,
		  `tanggal` date NOT NULL,
		  `catatan` varchar(512) NOT NULL,
		  `jumlahUang` double NOT NULL,
		  `kodePelanggan` varchar(64) NOT NULL,
		  `noAkunKas` varchar(10) NOT NULL,
		  `noAkunUangMuka` int(11) NOT NULL
		) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

		-- --------------------------------------------------------

		--
		-- Table structure for table `gd_user`
		--

		CREATE TABLE IF NOT EXISTS `gd_user` (
		`id` int(11) NOT NULL,
		  `username` varchar(64) NOT NULL,
		  `password` varchar(64) NOT NULL,
		  `level` tinyint(4) NOT NULL,
		  `lastActivity` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
		) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

		--
		-- Indexes for dumped tables
		--

		--
		-- Indexes for table `gd_bank`
		--
		ALTER TABLE `gd_bank`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodeRekening` (`kodeRekening`,`nomorRekening`);

		--
		-- Indexes for table `gd_bank_keluar`
		--
		ALTER TABLE `gd_bank_keluar`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_bank_masuk`
		--
		ALTER TABLE `gd_bank_masuk`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_bayar`
		--
		ALTER TABLE `gd_bayar`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_buku_besar`
		--
		ALTER TABLE `gd_buku_besar`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_data_departemen`
		--
		ALTER TABLE `gd_data_departemen`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_data_gudang`
		--
		ALTER TABLE `gd_data_gudang`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodeGudang` (`kodeGudang`);

		--
		-- Indexes for table `gd_data_pajak`
		--
		ALTER TABLE `gd_data_pajak`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodePajak` (`kodePajak`);

		--
		-- Indexes for table `gd_data_penyimpanan`
		--
		ALTER TABLE `gd_data_penyimpanan`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_data_produk`
		--
		ALTER TABLE `gd_data_produk`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodeBarang` (`kodeBarang`);

		--
		-- Indexes for table `gd_detail_bank_keluar`
		--
		ALTER TABLE `gd_detail_bank_keluar`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_detail_bank_masuk`
		--
		ALTER TABLE `gd_detail_bank_masuk`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_detail_kas_keluar`
		--
		ALTER TABLE `gd_detail_kas_keluar`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_detail_kas_masuk`
		--
		ALTER TABLE `gd_detail_kas_masuk`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_detail_transaksi_jurnal`
		--
		ALTER TABLE `gd_detail_transaksi_jurnal`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_fase_proyek`
		--
		ALTER TABLE `gd_fase_proyek`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_harta_tetap`
		--
		ALTER TABLE `gd_harta_tetap`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_hutang`
		--
		ALTER TABLE `gd_hutang`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_invoice_penjualan`
		--
		ALTER TABLE `gd_invoice_penjualan`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_jurnal_memorial`
		--
		ALTER TABLE `gd_jurnal_memorial`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_kas_keluar`
		--
		ALTER TABLE `gd_kas_keluar`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_kas_masuk`
		--
		ALTER TABLE `gd_kas_masuk`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_kelompok_barang`
		--
		ALTER TABLE `gd_kelompok_barang`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodeKelompok` (`kodeKelompok`);

		--
		-- Indexes for table `gd_kelompok_transaksi`
		--
		ALTER TABLE `gd_kelompok_transaksi`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodeKelompok` (`kodeKelompok`);

		--
		-- Indexes for table `gd_klasifikasi`
		--
		ALTER TABLE `gd_klasifikasi`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `noKlasifikasi` (`noKlasifikasi`);

		--
		-- Indexes for table `gd_mata_uang`
		--
		ALTER TABLE `gd_mata_uang`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodeMatauang` (`kodeMatauang`);

		--
		-- Indexes for table `gd_nama_alamat`
		--
		ALTER TABLE `gd_nama_alamat`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodePelanggan` (`kodePelanggan`);

		--
		-- Indexes for table `gd_order_pembelian`
		--
		ALTER TABLE `gd_order_pembelian`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodeTransaksi` (`kodeTransaksi`);

		--
		-- Indexes for table `gd_order_penjualan`
		--
		ALTER TABLE `gd_order_penjualan`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_pembelian_barang`
		--
		ALTER TABLE `gd_pembelian_barang`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_periode_akuntansi`
		--
		ALTER TABLE `gd_periode_akuntansi`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_piutang`
		--
		ALTER TABLE `gd_piutang`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_proyek`
		--
		ALTER TABLE `gd_proyek`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodeProyek` (`kodeProyek`);

		--
		-- Indexes for table `gd_rekening_jurnal`
		--
		ALTER TABLE `gd_rekening_jurnal`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `noAkun` (`noAkun`);

		--
		-- Indexes for table `gd_satuan_pengukuran`
		--
		ALTER TABLE `gd_satuan_pengukuran`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_tabel_info_perusahaan`
		--
		ALTER TABLE `gd_tabel_info_perusahaan`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodePerusahaan` (`kodePerusahaan`);

		--
		-- Indexes for table `gd_top`
		--
		ALTER TABLE `gd_top`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_tos`
		--
		ALTER TABLE `gd_tos`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodeTOS` (`kodeTOS`);

		--
		-- Indexes for table `gd_transaksi_jurnal`
		--
		ALTER TABLE `gd_transaksi_jurnal`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `kodeTransaksi` (`kodeTransaksi`);

		--
		-- Indexes for table `gd_uang_muka`
		--
		ALTER TABLE `gd_uang_muka`
		 ADD PRIMARY KEY (`id`);

		--
		-- Indexes for table `gd_user`
		--
		ALTER TABLE `gd_user`
		 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `username` (`username`);

		--
		-- AUTO_INCREMENT for dumped tables
		--

		--
		-- AUTO_INCREMENT for table `gd_bank`
		--
		ALTER TABLE `gd_bank`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_bank_keluar`
		--
		ALTER TABLE `gd_bank_keluar`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
		--
		-- AUTO_INCREMENT for table `gd_bank_masuk`
		--
		ALTER TABLE `gd_bank_masuk`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
		--
		-- AUTO_INCREMENT for table `gd_bayar`
		--
		ALTER TABLE `gd_bayar`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_buku_besar`
		--
		ALTER TABLE `gd_buku_besar`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=9;
		--
		-- AUTO_INCREMENT for table `gd_data_departemen`
		--
		ALTER TABLE `gd_data_departemen`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
		--
		-- AUTO_INCREMENT for table `gd_data_gudang`
		--
		ALTER TABLE `gd_data_gudang`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_data_pajak`
		--
		ALTER TABLE `gd_data_pajak`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
		--
		-- AUTO_INCREMENT for table `gd_data_penyimpanan`
		--
		ALTER TABLE `gd_data_penyimpanan`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_data_produk`
		--
		ALTER TABLE `gd_data_produk`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=9;
		--
		-- AUTO_INCREMENT for table `gd_detail_bank_keluar`
		--
		ALTER TABLE `gd_detail_bank_keluar`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
		--
		-- AUTO_INCREMENT for table `gd_detail_bank_masuk`
		--
		ALTER TABLE `gd_detail_bank_masuk`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
		--
		-- AUTO_INCREMENT for table `gd_detail_kas_keluar`
		--
		ALTER TABLE `gd_detail_kas_keluar`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=9;
		--
		-- AUTO_INCREMENT for table `gd_detail_kas_masuk`
		--
		ALTER TABLE `gd_detail_kas_masuk`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=10;
		--
		-- AUTO_INCREMENT for table `gd_detail_transaksi_jurnal`
		--
		ALTER TABLE `gd_detail_transaksi_jurnal`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=33;
		--
		-- AUTO_INCREMENT for table `gd_fase_proyek`
		--
		ALTER TABLE `gd_fase_proyek`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_harta_tetap`
		--
		ALTER TABLE `gd_harta_tetap`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_hutang`
		--
		ALTER TABLE `gd_hutang`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_invoice_penjualan`
		--
		ALTER TABLE `gd_invoice_penjualan`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=11;
		--
		-- AUTO_INCREMENT for table `gd_jurnal_memorial`
		--
		ALTER TABLE `gd_jurnal_memorial`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
		--
		-- AUTO_INCREMENT for table `gd_kas_keluar`
		--
		ALTER TABLE `gd_kas_keluar`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
		--
		-- AUTO_INCREMENT for table `gd_kas_masuk`
		--
		ALTER TABLE `gd_kas_masuk`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
		--
		-- AUTO_INCREMENT for table `gd_kelompok_barang`
		--
		ALTER TABLE `gd_kelompok_barang`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_kelompok_transaksi`
		--
		ALTER TABLE `gd_kelompok_transaksi`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=24;
		--
		-- AUTO_INCREMENT for table `gd_klasifikasi`
		--
		ALTER TABLE `gd_klasifikasi`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=8;
		--
		-- AUTO_INCREMENT for table `gd_mata_uang`
		--
		ALTER TABLE `gd_mata_uang`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_nama_alamat`
		--
		ALTER TABLE `gd_nama_alamat`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=17;
		--
		-- AUTO_INCREMENT for table `gd_order_pembelian`
		--
		ALTER TABLE `gd_order_pembelian`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_order_penjualan`
		--
		ALTER TABLE `gd_order_penjualan`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=17;
		--
		-- AUTO_INCREMENT for table `gd_pembelian_barang`
		--
		ALTER TABLE `gd_pembelian_barang`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
		--
		-- AUTO_INCREMENT for table `gd_periode_akuntansi`
		--
		ALTER TABLE `gd_periode_akuntansi`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_piutang`
		--
		ALTER TABLE `gd_piutang`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=35;
		--
		-- AUTO_INCREMENT for table `gd_proyek`
		--
		ALTER TABLE `gd_proyek`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=9;
		--
		-- AUTO_INCREMENT for table `gd_rekening_jurnal`
		--
		ALTER TABLE `gd_rekening_jurnal`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=91;
		--
		-- AUTO_INCREMENT for table `gd_satuan_pengukuran`
		--
		ALTER TABLE `gd_satuan_pengukuran`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=15;
		--
		-- AUTO_INCREMENT for table `gd_tabel_info_perusahaan`
		--
		ALTER TABLE `gd_tabel_info_perusahaan`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_top`
		--
		ALTER TABLE `gd_top`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_tos`
		--
		ALTER TABLE `gd_tos`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
		--
		-- AUTO_INCREMENT for table `gd_transaksi_jurnal`
		--
		ALTER TABLE `gd_transaksi_jurnal`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=10;
		--
		-- AUTO_INCREMENT for table `gd_uang_muka`
		--
		ALTER TABLE `gd_uang_muka`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
		--
		-- AUTO_INCREMENT for table `gd_user`
		--
		ALTER TABLE `gd_user`
		MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
		/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
		/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
		/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

		"""

		
		pass
	
	def Execute(self):
		#~ f = open("creator.md","w")
		#~ f.write(self.sqldump)
		#~ f.close()
		#~ f = open("creator.md","r")
		#~ subprocess.check_call(self.si_om.BasePath[:-1]+"\\mysql\\bin\\mysql.exe --port=44559 -u root test",stdin=f,shell=True)
		#~ f.close()
		#~ subprocess.check_call(self.si_om.BasePath+"mysql/bin/echo.exe < "+"creator.md")
		#~ self.si_om.DatabaseRunQuery(self.sqldump)
		#---- ga bisa pakai runQuery --- commit harus menunggu beberapa detik
		#---- new attempt: exclusive mysqldb
		try:
			self.db = MySQLdb.connect(self.si_om.dbHost,self.si_om.dbUser,self.si_om.dbPass,self.si_om.dbDatabase)
			print ("connected database to generic mysql port")
		except:
			try:
				print "gagal"
				self.db = MySQLdb.Connect(host=self.si_om.dbHost, port=self.si_om.dbPort, user=self.si_om.dbUser, passwd=self.si_om.dbPass, db=self.si_om.dbDatabase)
				print ("connected database to Garvin port")
			except:
				print "gagal"
				#~ exit (1)
		#-- sudah terkoneksi, bentuk cursor
		try:
			self.cursor = self.db.cursor()
		except:return
		self.cursor.execute(self.sqldump)
		self.creatortimer = QtCore.QTimer(self.si_om)
		self.creatortimer.timeout.connect(self.Selesai)
		self.creatortimer.start(4000)
		
	def Selesai(self):
		self.db.commit()
		self.creatortimer.stop()
		print "commited"
		self.db.close()
		
	def close(self):
		self.sqldump=None
		self.si_om=None
		#--- let the garbage collector work

